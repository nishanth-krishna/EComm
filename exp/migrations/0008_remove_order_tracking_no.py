# Generated by Django 3.2.5 on 2022-05-26 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exp', '0007_auto_20220526_0706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tracking_no',
        ),
    ]
