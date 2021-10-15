from album.models import Album
from picture.models import Picture


def delete_album_with_images(instance):
    pictures = Album.objects.get_pictures(instance.id)
    picture_to_delete_ids = []
    for p in pictures:
        if p.get('count') == 1:
            picture_id = p.get('picture_id')
            picture_to_delete_ids.append(picture_id)
    Picture.objects.filter(id__in=picture_to_delete_ids).delete()
    instance.delete()





