# Generated by Django 3.2.7 on 2021-10-10 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('picture', '0002_alter_picture_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'album',
            },
        ),
        migrations.CreateModel(
            name='AlbumPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='album.album')),
                ('picture', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='picture.picture')),
            ],
            options={
                'db_table': 'album_picture',
            },
        ),
    ]
