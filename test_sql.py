#exec(open('test_sql.py').read())
from picture import utils
from picture.models import Picture
print([p.picture_info__width for p in utils.transform_width_height(Picture.objects.all(), measurement='cm')])
