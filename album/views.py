from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from album.models import Album
from album.serializers import AlbumSerializer, AddImagesSerializer
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
            self.permission_classes = [IsResourceOwner, permissions.IsAdminUser]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == 'add_image_to_album':
            self.serializer_class = AddImagesSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    @action(methods=['post'], detail=True)
    def add_image_to_album(self, request, id=None):
        album = self.get_object()
        user = request.user
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(album=album)
        return Response('Salam')



