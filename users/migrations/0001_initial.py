# Generated by Django 2.2.1 on 2019-06-20 21:37

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('acads', '0001_initial'),
        ('privilege', '0001_initial'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('roll', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('program', models.CharField(max_length=20)),
                ('dept', models.CharField(max_length=50)),
                ('hall', models.CharField(max_length=15)),
                ('room', models.CharField(max_length=20)),
                ('blood_group', models.CharField(max_length=14)),
                ('gender', models.CharField(max_length=10)),
                ('hometown', models.CharField(max_length=100)),
                ('fblink', models.URLField(max_length=120, null=True)),
                ('por', django.contrib.postgres.fields.jsonb.JSONField(default=dict, null=True)),
                ('earlier_login', models.BooleanField(default=0, null=True)),
                ('acads', models.ManyToManyField(to='acads.AcadsModel')),
                ('owned', models.ManyToManyField(through='privilege.privileges', to='tags.TagModel')),
                ('tags', models.ManyToManyField(related_name='tags', to='tags.TagModel')),
            ],
        ),
    ]
