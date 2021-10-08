from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

class Picture(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    user = models.ForeignKey(User, blank=False, related_name='user_picture', null=False, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media', null=False, blank=False)
    likes = models.PositiveIntegerField(null=False, blank=False, default=0)

    def get_absolute_url(self):
        pass

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'picture'

