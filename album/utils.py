from album.models import Album
from picture.models import Picture
from django.conf import settings

def delete_album_with_images(instance):
    pictures = Album.objects.get_pictures(instance.id)
    picture_to_delete_ids = []
    for p in pictures:
        if p.get('count') == 1:
            picture_id = p.get('picture_id')
            picture_to_delete_ids.append(picture_id)
            picture = Picture.objects.get(id=picture_id)
            delete_image_from_s3(picture.image)
            
    Picture.objects.filter(id__in=picture_to_delete_ids).delete()
    instance.delete()


def delete_image_from_s3(image):
    import boto3

    s3 = boto3.resource('s3')    
    s3.Object(settings.AWS_STORAGE_BUCKET_NAME, image.name).delete()
    