from rest_framework import serializers

from picture.models import Picture


class PictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Picture
        fields = '__all__'
        read_only_fields = ['user']

