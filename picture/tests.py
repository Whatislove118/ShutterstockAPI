from django.test import TestCase

from picture.models import Picture
from .utils import get_metadata_from_s3
# Create your tests here.

class TestGetMetadata(TestCase):
    
    def test_get(self):
        instance = Picture.objects.get(id=4)
        get_metadata_from_s3(instance)
        