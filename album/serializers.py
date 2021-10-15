from django.apps import apps
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from album.models import Album, AlbumPicture
from picture.models import Picture


class AlbumSerializer(serializers.ModelSerializer):
    album_pictures = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='picture:retrieve-picture', lookup_field='id')

    class Meta:
        model = Album
        fields = '__all__'
        read_only_fields = ['user']


class AddImagesSerializer(AlbumSerializer):
    album_pictures = serializers.PrimaryKeyRelatedField(many=True, queryset=Picture.objects.all())

    class Meta(AlbumSerializer.Meta):
        fields = None
        exclude = ['name']

    # TODO попробовать вынести логику
    def save(self, **kwargs):
        album = kwargs.pop('album')
        pictures = self.validated_data.pop('album_pictures')
        for p in pictures:
            try:
                album.album_pictures.through.objects.get(picture=p, album=album)
                raise ValidationError({"detail": "picture with id=%d is already exists in album %s" % (p.id, album.name)}, code=400)
            except AlbumPicture.DoesNotExist:
                album.album_pictures.add(p)
        return album

