from datetime import datetime
from enum import unique

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Manager, F
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save
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


def generate_upload_url(instance, filename):
    return "%s/%s/%s" % (instance.user.username, instance.name, filename)

# важное замечание - blank - по сути указывает будет ли обязательным внутри кода django, null - на уровне бд
class Picture(models.Model):
    name = models.CharField(max_length=255, blank=False)
    user = models.ForeignKey(User,  related_name='user_picture', null=False, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=generate_upload_url, unique=True)
    date_of_published = models.DateTimeField(blank=False, default=datetime.now())
    likes = models.PositiveIntegerField(null=False, blank=False, default=0)
    album = models.ManyToManyField(Album, through=AlbumPicture, related_name='album_pictures', blank=True)
    category = models.CharField(max_length=255, blank=False, choices=PictureCategoryChoices.choices, null=False)
    is_notify = models.BooleanField(default=False)

    objects = PictureManager()
    
    
    def like(self):
        self.likes += 1
        self.save(update_fields=['likes'])
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date_of_published']
        db_table = 'picture'


class PictureInfo(models.Model):
    picture = models.OneToOneField('picture.Picture', related_name='picture_info', to_field='image', blank=False, null=False, unique=True, on_delete=models.CASCADE)
    extension = models.CharField(max_length=100, blank=False)
    size = models.PositiveBigIntegerField(default=0)

    class Meta:
        db_table = 'picture_info'
        





