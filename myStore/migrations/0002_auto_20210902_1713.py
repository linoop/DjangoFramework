# Generated by Django 3.2.7 on 2021-09-02 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myStore', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='Books',
        ),
        migrations.RenameModel(
            old_name='Game',
            new_name='Games',
        ),
    ]
