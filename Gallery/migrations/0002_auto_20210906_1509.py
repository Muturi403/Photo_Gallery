# Generated by Django 3.2.7 on 2021-09-06 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='location_id',
            new_name='location',
        ),
    ]
