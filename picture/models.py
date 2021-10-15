from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Manager, F
from rest_framework.reverse import reverse

from album.models import Album, AlbumPicture

User = get_user_model()

class PictureCategoryChoices(models.TextChoices):
    PHOTO = 'PH', 'photo'
    VECTOR_GRAPHIC = 'VG', 'vectors_graphic'
    ILLUSTRATION = 'IL', 'illustration'

class PictureCategory(models.Model):
    name = models.CharField(max_length=100, blank=False, choices=PictureCategoryChoices.choices, unique=True)

    # чтобы убрать возможность создания обьектов при save с любым именем, создадим constraint
    class Meta:
        db_table = 'picture_category'
        constraints = [
            models.CheckConstraint(
                name='%(app_label)s_%(class)s_name_invalid',
                check=models.Q(name__in=PictureCategoryChoices.values)
            )
        ]

    def __str__(self):
        return 'PictureCategory - %s' % self.name


class PictureManager(models.Manager):

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def get_with_picture_info(self, id=None, measurement='px'):
        return self.transform_width_height(id)







# важное замечание - blank - по сути указывает будет ли обязательным внутри кода django, null - на уровне бд
class Picture(models.Model):
    name = models.CharField(max_length=255, blank=False)
    user = models.ForeignKey(User,  related_name='user_picture', null=False, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media')
    date_of_published = models.DateTimeField(blank=False, default=datetime.now())
    likes = models.PositiveIntegerField(null=False, blank=False, default=0)
    album = models.ManyToManyField(Album, through=AlbumPicture, related_name='album_pictures', blank=True)
    category = models.ForeignKey('PictureCategory', blank=False, null=False, on_delete=models.DO_NOTHING)

    objects = PictureManager()

    def get_absolute_url(self):
        return reverse('retrieve-update-destroy-picture', kwargs={'id': self.id})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date_of_published']
        db_table = 'picture'


class PictureExtensionsChoices(models.TextChoices):
    JPEG = 'JPEG', 'jpeg'
    PNG = 'PNG', 'png'
    SVG = 'SVG', 'svg'


class PictureInfo(models.Model):
    picture = models.OneToOneField('picture.Picture', related_name='picture_info', blank=False, null=False, on_delete=models.CASCADE)
    width = models.PositiveIntegerField(default=0, blank=False)
    height = models.PositiveIntegerField(default=0, blank=False)
    extension = models.CharField(max_length=100, choices=PictureExtensionsChoices.choices, blank=False)
    size = models.PositiveBigIntegerField(default=0)

    class Meta:
        db_table = 'picture_info'
        constraints = [
            models.CheckConstraint(
                name='%(app_label)s_%(class)s_extension_invalid',
                check=models.Q(extension__in=PictureExtensionsChoices.values)
            )
        ]

