# Generated by Django 2.1 on 2018-08-21 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
