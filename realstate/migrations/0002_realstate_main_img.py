# Generated by Django 3.2 on 2022-10-13 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realstate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='realstate',
            name='main_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
