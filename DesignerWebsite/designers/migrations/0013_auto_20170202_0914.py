# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-02 03:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designers', '0012_auto_20170202_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designers',
            name='design2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='designers',
            name='design3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]