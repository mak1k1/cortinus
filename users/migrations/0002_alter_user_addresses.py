# Generated by Django 4.0.4 on 2022-04-21 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='addresses',
            field=models.ManyToManyField(blank=True, to='users.address'),
        ),
    ]
