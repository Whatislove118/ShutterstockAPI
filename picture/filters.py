from django_filters import rest_framework as django_filters

from picture.models import Picture, PictureCategory


class SearchFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='exact')

    class Meta:
        model = Picture
        fields = ['q', 'category']





