# Generated by Django 3.2.8 on 2021-10-23 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userproperties_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userproperties',
            name='image',
        ),
    ]