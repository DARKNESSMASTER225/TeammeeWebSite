# Generated by Django 4.2.5 on 2023-10-20 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_file_remove_profile_access_level_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='admin',
            new_name='owner',
        ),
        migrations.RemoveField(
            model_name='group',
            name='members',
        ),
        migrations.RemoveField(
            model_name='group',
            name='viewers',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='group_id',
        ),
        migrations.AddField(
            model_name='profile',
            name='access_layer',
            field=models.IntegerField(default=0),
        ),
    ]