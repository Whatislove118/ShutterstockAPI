from django.conf.urls import url
from django.urls import path
from picture.models import Picture

from picture.views import PictureViewSet

app_name = 'picture'

retrieve_update_delete_picture = PictureViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'put': 'update',
    'delete': 'destroy'
})

list_create_picture = PictureViewSet.as_view({
    'post': 'create',
    'get': 'list',
})


urlpatterns = [
    path('', list_create_picture, name='list-picture'),
    path('<int:id>/', retrieve_update_delete_picture, name='retrieve-picture'),
    path('<int:id>/like/', PictureViewSet.as_view(
        {
            'post': 'like'
        }
    ), name='like=picture')
    # path('test/', func)
]