# Generated by Django 3.2 on 2022-10-13 19:09

from django.db import migrations, models
import realstate.models


class Migration(migrations.Migration):

    dependencies = [
        ('realstate', '0002_realstate_main_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realstate',
            name='main_img',
            field=models.ImageField(blank=True, null=True, upload_to=realstate.models.path_file_name),
        ),
    ]
