# Generated by Django 3.2.5 on 2022-05-26 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exp', '0006_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tracking_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
