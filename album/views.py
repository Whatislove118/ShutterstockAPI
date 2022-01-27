from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from album.models import Album
from album.serializers import AlbumSerializer, AddImagesSerializer
from album.utils import delete_album_with_images
from picture.permissions import IsResourceOwner


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'
    model = Album
    serializer_class = AlbumSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [permissions.IsAuthenticated]
        if self.action in ('update', 'partial_update', 'add_image_to_album'):
            self.permission_classes = [IsResourceOwner]
        if self.action == 'destroy':
            self.permission_classes = [IsResourceOwner | permissions.IsAdminUser]
        return super().get_permissions()



    def get_serializer_class(self):
        if self.action == 'add_image_to_album':
            self.serializer_class = AddImagesSerializer
        return super().get_serializer_class()




    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    ''' 
        Необходимо при удалении альбома удалять и картинки при условии, что картинка принадлежит только этому альбому
        Я реализую метод в менеджере который будет удалять фотографию, если количество ее использований будет меньше 2
        Данный вариант был выбран из за того, что функция count - агрегатная, и быстрая по большим данным
    '''

    def get_queryset(self):
        if self.action == 'add_image_to_album':
            self.queryset = self.queryset.prefetch_related('album_pictures')
        return super().get_queryset()

    # def get_object(self):
    #     if self.action == 'add_image_to_album':
    #
    #     return super().get_object()

    def perform_destroy(self, instance):
        delete_album_with_images(instance)


    @action(methods=['post'], detail=True)
    def add_image_to_album(self, request, id=None):
        album = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(album=album)
        return Response({"detail": "ok"})



