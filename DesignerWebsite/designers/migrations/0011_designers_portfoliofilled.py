# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-02 00:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designers', '0010_auto_20170201_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='designers',
            name='PortfolioFilled',
            field=models.BooleanField(default=False),
        ),
    ]
