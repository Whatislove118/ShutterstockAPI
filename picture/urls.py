from django.conf.urls import url
from django.urls import path

from picture.views import PictureViewSet

retrieve_update_delete_picture = PictureViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'put': 'update',
    'delete': 'destroy'
})
create_picture = PictureViewSet.as_view({
    'post': 'create'
})
list_picture = PictureViewSet.as_view({
    'get': 'list'
})

urlpatterns = [
    path('all/', list_picture, name='list-picture'),
    path('<int:id>/', retrieve_update_delete_picture, name='retrieve-picture'),
    path('', create_picture, name='create-picture'),
]