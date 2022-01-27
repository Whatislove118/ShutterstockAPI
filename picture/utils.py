import os
from pydoc import cli
from re import I

from PIL import Image
from django.db.models import F
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_filters import rest_framework as django_filters
from rest_framework.views import exception_handler
from picture.models import Picture, PictureCategory, PictureInfo
from root import settings
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    
    if isinstance(exc, IntegrityError) and not response:
        response = Response(
            {
                'detail': 'It seems there is a conflict between the data you are trying to save and your current ' \
                           'data. Please review your entries and try again.'
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    return response
        

def transform_width_height(queryset, measurement='px'):
    if measurement == 'cm':
        queryset = queryset.select_related('picture_info').all()
        for picture in queryset:
            picture_info = picture.picture_info
            picture_info.width /= 10
            picture_info.height /= 10
        return queryset
    return queryset


class SearchFilter(django_filters.FilterSet):
    MEASUREMENT_CHOICES = (
        ('cm', 'cm'),
        ('px', 'px'),
    )

    q = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='exact')
    sort = django_filters.OrderingFilter(fields=(
        ('newest', 'oldest')),
        method='filter_sort') # привязка по методу отменяет стандартную фильтрацию поля
    min_width = django_filters.NumberFilter(field_name='picture_info__width', lookup_expr='gt')
    min_height = django_filters.NumberFilter(field_name='picture_info__height', lookup_expr='gt')
    measurement = django_filters.ChoiceFilter(method='filter_measurement', choices=MEASUREMENT_CHOICES)

    def filter_measurement(self, queryset, name, value):
        return transform_width_height(queryset, measurement=value)

    def filter_sort(self, queryset, name, value):
        if value[0] == 'newest':
            return queryset.order_by('-date_of_published')
        return queryset.order_by('date_of_published')

    class Meta:
        model = Picture
        fields = ['q', 'category', 'sort', 'measurement', 'min_width', 'min_height']


def get_metadata_from_s3(instance, bucket_name=settings.AWS_STORAGE_BUCKET_NAME):
    import boto3
    
    client = boto3.client('s3')
    try:
        metadata = client.head_object(Bucket=bucket_name, Key=instance.image.name)
    except:
        print("Failed {}".format(instance.image.name))
    data = {
        'picture': instance,
        'size': metadata.get('ContentLength'),
        'extension': metadata.get('ContentType')
    }
    return data

def format_bytes(size, round_count=2):
    power = 2**10
    n = 0
    power_labels = {0: '', 1: 'K', 2: 'M', 3: 'G'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, round_count)) + power_labels[n] + 'B'



@receiver(post_delete, sender=Picture, dispatch_uid='rm_picture_from_s3')
def remove_image_s3(sender, instance, **kwargs):
    try:
        instance.image.storage.delete()
    except:
        pass

@receiver(post_save, sender=Picture, dispatch_uid='create_picture_info_uid')
def create_picture_info_signal(sender, instance, created, **kwargs):
    if created:
        data = get_metadata_from_s3(instance)
        PictureInfo.objects.create(**data)