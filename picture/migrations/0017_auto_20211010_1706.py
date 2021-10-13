# Generated by Django 3.2.7 on 2021-10-10 14:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0016_alter_picture_date_of_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='picture.picturecategory'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='date_of_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 10, 17, 6, 5, 226581)),
        ),
    ]