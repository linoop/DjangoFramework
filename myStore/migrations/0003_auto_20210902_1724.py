# Generated by Django 3.2.7 on 2021-09-02 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myStore', '0002_auto_20210902_1713'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
        migrations.RenameModel(
            old_name='Games',
            new_name='Game',
        ),
    ]
