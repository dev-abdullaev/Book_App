# Generated by Django 3.1.4 on 2021-01-25 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0007_auto_20210125_2245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='my_file',
            new_name='Upload_File',
        ),
    ]
