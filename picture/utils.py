import os

from PIL import Image
from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_filters import rest_framework as django_filters

from picture.models import Picture, PictureCategory, PictureInfo


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


@receiver(post_save, sender=Picture, dispatch_uid='create_picture_info_uid')
def create_picture_info_signal(sender, instance, created, **kwargs):
    data = _generate_data_for_picture_info(instance)
    picture_info = PictureInfo.objects.get_or_create(**data)
    # print(picture_info.picture_id)

def _generate_data_for_picture_info(instance):
    image = Image.open(instance.image.path)
    data = {
        'picture': instance,
        'size': os.stat(instance.image.path).st_size,  # ????
        'width': image.width,
        'height': image.height,
        'extension': image.format
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



