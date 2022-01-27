from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from album.models import Album
from album.serializers import AlbumSerializer
from picture.models import Picture, PictureCategory, PictureInfo
from picture.utils import format_bytes


class PictureInfoSerializer(serializers.ModelSerializer):
    size = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = PictureInfo
        # fields = '__all__'
        exclude = ['picture']

    def get_size(self, obj):
        return format_bytes(obj.size)


class PictureSerializer(serializers.ModelSerializer):
    # likes = serializers.DecimalField(read_only=True, max_digits=10, decimal_places=2)
    # category = serializers.SlugRelatedField(many=False, read_only=False, queryset=PictureCategory.objects.all(), slug_field='name')
    picture_info = PictureInfoSerializer(read_only=True, many=False)
    album = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='album:retrieve-update-destroy-album', lookup_field='id')
    image = serializers.ImageField(max_length=None)
    
    class Meta:
        model = Picture
        fields = '__all__'
        read_only_fields = ['user', 'likes']

    # def validate(self, attrs):
    #     print("validate")
    #     return super().validate(attrs)
    #
    # def is_valid(self, raise_exception=False):
    #     print(str(self))
    #     print('is_valid')
    #     # print(self.validated_data)
    #     a = super().is_valid(raise_exception)
    #     print(self.validated_data)
    #     return a

    def save(self, **kwargs):
        print('save')
        return super().save(**kwargs)

    def create(self, validated_data):
        print("create")
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


# class PictureCreateSerializer(PictureSerializer):
#     album = serializers.PrimaryKeyRelatedField(many=False, write_only=True, queryset=Album.objects.all())
#
#     class Meta(PictureSerializer.Meta):
#         pass

    # #TODO вынести в другой класс + транзакция
    # def create(self, validated_data):
    #     album_from_request = validated_data.pop('album')
    #     picture = super().create(validated_data)
    #     picture.album.add(album_from_request)
    #     picture.save()
    #     print(picture.picture_album)
    #     return picture


