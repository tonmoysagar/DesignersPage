# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-14 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designers', '0005_auto_20170112_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='designers',
            name='address',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='designers',
            name='contact',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='designers',
            name='design',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='designers',
            name='email',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='designers',
            name='firmname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='designers',
            name='name',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='designers',
            name='password',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
