# Generated by Django 3.2.7 on 2022-01-27 10:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0007_alter_album_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 27, 13, 57, 43, 647958)),
        ),
    ]
