from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    user = models.OneToOneField(User, blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'album'

class AlbumPicture(models.Model):
    picture = models.ForeignKey('picture.Picture', blank=False, null=False, on_delete=models.DO_NOTHING)
    album = models.ForeignKey(Album, blank=False, null=False, on_delete=models.DO_NOTHING)



    class Meta:
        db_table = 'album_picture'
