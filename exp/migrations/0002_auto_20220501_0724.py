# Generated by Django 3.2.5 on 2022-05-01 07:24

from django.db import migrations, models
import exp.models


class Migration(migrations.Migration):

    dependencies = [
        ('exp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_image',
            new_name='product_image_1',
        ),
        migrations.AddField(
            model_name='product',
            name='product_image_2',
            field=models.ImageField(blank=True, null=True, upload_to=exp.models.get_file_path),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image_3',
            field=models.ImageField(blank=True, null=True, upload_to=exp.models.get_file_path),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image_4',
            field=models.ImageField(blank=True, null=True, upload_to=exp.models.get_file_path),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image_5',
            field=models.ImageField(blank=True, null=True, upload_to=exp.models.get_file_path),
        ),
    ]