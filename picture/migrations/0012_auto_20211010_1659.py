# Generated by Django 3.2.7 on 2021-10-10 13:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0011_auto_20211010_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='date_of_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 10, 16, 59, 52, 592318)),
        ),
        migrations.AlterField(
            model_name='picture',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]