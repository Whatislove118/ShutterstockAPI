from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from picture.models import Picture, PictureCategory


class PictureSerializer(serializers.ModelSerializer):
    # likes = serializers.DecimalField(read_only=True, max_digits=10, decimal_places=2)
    category = serializers.SlugRelatedField(many=False, read_only=False, queryset=PictureCategory.objects.all(), slug_field='name')


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




