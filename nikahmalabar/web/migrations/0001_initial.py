# Generated by Django 3.2.8 on 2021-10-23 04:45

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilecode', models.CharField(max_length=225)),
                ('name', models.CharField(max_length=225)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='male', max_length=225)),
                ('age', models.CharField(max_length=225)),
                ('status', models.CharField(choices=[('single', 'Single'), ('divorced', 'Divorced')], default='single', max_length=225)),
                ('relegion', models.CharField(max_length=225)),
                ('highereducation', models.CharField(max_length=225)),
                ('job', models.CharField(max_length=225)),
                ('place', models.CharField(max_length=225)),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='Profile/', verbose_name='Profile')),
            ],
            options={
                'verbose_name_plural': 'Profile',
            },
        ),
    ]
