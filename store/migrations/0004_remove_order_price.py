# Generated by Django 4.0.4 on 2022-04-21 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
    ]
