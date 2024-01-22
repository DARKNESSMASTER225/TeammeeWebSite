# Generated by Django 5.0.1 on 2024-01-22 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auditlog', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auditlogmodel',
            name='file',
        ),
        migrations.AddField(
            model_name='auditlogmodel',
            name='file_name',
            field=models.CharField(default=datetime.datetime(2024, 1, 22, 17, 48, 32, 595121), max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='auditlogmodel',
            name='group',
            field=models.ManyToManyField(to='users.group'),
        ),
        migrations.AlterField(
            model_name='auditlogmodel',
            name='comment',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
