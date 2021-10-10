from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

from album.models import Album, AlbumPicture

User = get_user_model()

class PictureChoices(models.TextChoices):
    PHOTO = 'PH', 'photo'
    VECTOR_GRAPHIC = 'VG', 'vectors_graphic'
    ILLUSTRATION = 'IL', 'illustration'

class PictureCategory(models.Model):
    name = models.CharField(max_length=100, blank=False, choices=PictureChoices.choices, unique=True)

    # чтобы убрать возможность создания обьектов при save с любым именем, создадим constraint
    class Meta:
        db_table = 'picture_category'
        constraints = [
            models.CheckConstraint(
                name='%(app_label)s_%(class)s_name_invalid',
                check=models.Q(name__in=PictureChoices.values)
            )
        ]

    def __str__(self):
        return 'PictureCategory - %s' % self.name


# важное замечание - blank - по сути указывает будет ли обязательным внутри кода django, null - на уровне бд
class Picture(models.Model):
    name = models.CharField(max_length=255, blank=False)
    user = models.ForeignKey(User,  related_name='user_picture', null=False, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media')
    date_of_published = models.DateTimeField(blank=False, default=datetime.now())
    likes = models.PositiveIntegerField(null=False, blank=False, default=0)
    album = models.ManyToManyField(Album, through=AlbumPicture, related_name='album_pictures', blank=True)
    category = models.ForeignKey('PictureCategory', blank=False, null=False, on_delete=models.DO_NOTHING)

    def get_absolute_url(self):
        pass

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'picture'

