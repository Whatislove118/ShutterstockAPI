from django.contrib import admin

# Register your models here.
from picture.models import PictureCategory


@admin.register(PictureCategory)
class PictureCategoryAdmin(admin.ModelAdmin):
    pass

