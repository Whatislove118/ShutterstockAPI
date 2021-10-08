from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions

from picture.models import Picture
from picture.serializers import PictureSerializer
from .permissions import IsResourceOwner


class PictureViewSet(viewsets.ModelViewSet):
    model = Picture
    permission_classes = [permissions.AllowAny]
    queryset = Picture.objects.all()
    lookup_field = 'id'
    serializer_class = PictureSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [permissions.IsAuthenticated]
        if self.action == 'update' or self.action == 'destroy' or self.action == 'partial_update':
            self.permission_classes = [IsResourceOwner]
        return super().get_permissions()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)



