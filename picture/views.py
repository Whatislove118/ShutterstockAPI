# from django_filters import rest_framework as filters


# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.decorators import parser_classes, renderer_classes
from picture.models import Picture
from picture.serializers import PictureSerializer
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from . import utils
from .permissions import IsResourceOwner
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import send_message

class PictureViewSet(viewsets.ModelViewSet):
    model = Picture
    permission_classes = [permissions.AllowAny]
    queryset = Picture.objects.all()
    lookup_field = 'id'
    serializer_class = PictureSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = utils.SearchFilter
    parser_classes = [MultiPartParser]
    # filterset_fields = ['category']

    def create(self, request, *args, **kwargs):        
        return super().create(request, *args, **kwargs)

    def get_permissions(self):
        if self.action in ('create', 'like'):
            self.permission_classes = [permissions.IsAuthenticated]
        if self.action in ('update', 'destroy', 'partial_updae'):
            self.permission_classes = [IsResourceOwner]
        return super().get_permissions()

    def perform_create(self, serializer):
        print('perform_create')
        user = self.request.user
        serializer.save(user=user)

    def get_object(self, **kwargs):
        # print(self.kwargs.get(self.lookup_field))
        print('get_object')
        obj = super().get_object()
        return obj

    @action(methods=['POST'], detail=True)
    def like(self, request, *args, **kwargs):
        instance = self.get_object()
        # instance.like()
        send_message(instance.id)
        return Response({'detail': 'ok.'})
    # def get_serializer_class(self):
    #     if self.action == 'create':
    #         self.serializer_class = PictureCreateSerializer
    #     return super().get_serializer_class()

    # def filter_queryset(self, queryset):
    #     print('filter_queryset')
    #     queryset = super().filter_queryset(queryset)
    #     print([p.picture_info.width for p in queryset.all()])
    #     return queryset


    # def get_queryset(self):
    #
    #     return self.queryset




@api_view(["GET"])
def health(request):
    if request.method == 'GET':
        instance = Picture.objects.get(id=4)
        utils.get_metadata_from_s3(instance)
        return Response({"detail": "ok"})