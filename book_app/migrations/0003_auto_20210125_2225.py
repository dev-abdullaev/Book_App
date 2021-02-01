# Generated by Django 3.1.4 on 2021-01-25 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0002_uploadmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UploadModel',
        ),
        migrations.AddField(
            model_name='book',
            name='my_file',
            field=models.FileField(default=11, upload_to='media/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]