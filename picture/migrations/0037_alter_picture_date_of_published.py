# Generated by Django 3.2.7 on 2021-10-13 16:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0036_alter_picture_date_of_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='date_of_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 13, 19, 37, 23, 806124)),
        ),
    ]