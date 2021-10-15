#exec(open('test_sql.py').read())
# from django.db.models import Count
#
# from album.models import Album
# from picture import utils
# from picture.models import Picture
# # print([p.picture_info__width for p in utils.transform_width_height(Picture.objects.all(), measurement='cm')])
# queryset = Album.objects.prefetch_related('album_pictures').annotate(count=Count('album_pictures__picture_album'))
#
# stores = []
#
# for store in queryset:
#     stores.append({'id': store.id, 'name': store.count, 'books': store})
#
# print(stores)
#
#
#     # .filter(album_pictures__album=5).values('album_pictures__picture', 'album_pictures__album').annotate(count=Count('album_pictures__picture_album'))
# # print(album.count)
from album.models import Album
from album.utils import delete_album_with_images

# pictures = Album.objects.get_pictures(16)
album = Album.objects.get(id=21)
delete_album_with_images(album)

# for p in pictures:
#     print(p.count)
