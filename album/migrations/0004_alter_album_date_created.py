# Generated by Django 3.2.7 on 2022-01-09 17:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0003_alter_album_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 9, 20, 13, 2, 456385)),
        ),
    ]
