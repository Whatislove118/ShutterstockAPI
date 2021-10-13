from django.urls import path

from album.views import AlbumViewSet


app_name = 'album'
create_album = AlbumViewSet.as_view({
    'post': 'create'
})

retrieve_update_delete_album = AlbumViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'put': 'update',
    'delete': 'destroy'
})

list_album = AlbumViewSet.as_view({
    'get': 'list'
})
add_image_to_album = AlbumViewSet.as_view({
    'post': 'add_image_to_album'
})
urlpatterns = [
    path('', create_album, name='create-album'),
    path('all/', list_album, name='list-album'),
    path('<int:id>/', retrieve_update_delete_album,
         name='retrieve-update-destroy-album'),
    path('<int:id>/add/', add_image_to_album, name='add-image')


]