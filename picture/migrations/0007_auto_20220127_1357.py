# Generated by Django 3.2.7 on 2022-01-27 10:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0006_auto_20220116_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='is_notify',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='picture',
            name='date_of_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 27, 13, 57, 43, 648959)),
        ),
    ]
