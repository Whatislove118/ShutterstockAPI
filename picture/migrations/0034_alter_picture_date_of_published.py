# Generated by Django 3.2.7 on 2021-10-12 19:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0033_auto_20211011_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='date_of_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 12, 22, 57, 44, 882214)),
        ),
    ]