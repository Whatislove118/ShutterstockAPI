# Generated by Django 3.2.7 on 2021-10-10 13:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0005_alter_picture_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PictureCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[], max_length=100)),
            ],
            options={
                'db_table': 'picture_category',
            },
        ),
        migrations.AddField(
            model_name='picture',
            name='date_of_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 10, 16, 51, 0, 799754)),
        ),
    ]
