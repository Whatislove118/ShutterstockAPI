# from django_filters import rest_framework as filters
from django.db.models import Q

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from picture.models import Picture
from picture.serializers import PictureSerializer
from . import filters
from .permissions import IsResourceOwner


class PictureViewSet(viewsets.ModelViewSet):
    model = Picture
    permission_classes = [permissions.AllowAny]
    queryset = Picture.objects.all()
    lookup_field = 'id'
    serializer_class = PictureSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.SearchFilter
    # filterset_fields = ['category']

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [permissions.IsAuthenticated]
        if self.action == 'update' or self.action == 'destroy' or self.action == 'partial_update':
            self.permission_classes = [IsResourceOwner]
        return super().get_permissions()

    def perform_create(self, serializer):
        print('perform_create')
        user = self.request.user
        serializer.save(user=user)

    def get_object(self, **kwargs):
        print(self.kwargs.get(self.lookup_field))
        print('get_object')
        return super().get_object()

    # def filter_queryset(self, queryset):
    #     print('filter_queryset')
    #     query = self.request.GET.get('q')
    #     if self.action == 'list' and query is not None:
    #         print('filtering')
    #         queryset = self.queryset.filter(Q(name__icontains=query))
    #         super().get_queryset()
    #     return super().filter_queryset(queryset)


    # def get_queryset(self):
    #     print("get_queryset")
    #     return self.queryset




