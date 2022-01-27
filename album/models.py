from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Manager, Count

User = get_user_model()


class AlbumManager(Manager):

    # def annotate_count_pictures(self, queryset):
    #     queryset.prefetch_related('album_pictures')

    def get_pictures(self, id=None):
        queryset = AlbumPicture.objects.select_related('picture').values('picture_id').annotate(count=Count('picture_id'))
        return queryset.all()


class Album(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now())

    objects = AlbumManager()

    class Meta:
        db_table = 'album'

    def delete(self, using=None, keep_parents=False):
        return super().delete(using, keep_parents)


class AlbumPicture(models.Model):
    picture = models.ForeignKey('picture.Picture', related_name='picture_album', blank=False, null=True,
                                on_delete=models.CASCADE)
    album = models.ForeignKey(Album, related_name='album_picture', blank=False, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'album_picture'
