# Generated by Django 3.2 on 2022-10-16 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realstate', '0013_rename_realstate_realstateimage_realstat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realstateimage',
            old_name='realstat',
            new_name='realstate',
        ),
    ]
