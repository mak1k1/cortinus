# Generated by Django 4.0.2 on 2022-03-19 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_category_level_category_lft_category_rght_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='level',
        ),
        migrations.RemoveField(
            model_name='category',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='category',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='category',
            name='tree_id',
        ),
    ]
