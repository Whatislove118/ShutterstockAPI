# Generated by Django 3.2.7 on 2022-01-15 13:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0004_alter_album_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 15, 16, 57, 15, 637481)),
        ),
    ]
