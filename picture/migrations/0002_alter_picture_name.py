# Generated by Django 3.2.7 on 2021-10-08 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]