# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-02 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designers', '0011_designers_portfoliofilled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designers',
            name='AboutMe',
            field=models.TextField(default='Please tell us about your personallity and why shoud customers be interested in you', max_length=200, null=True),
        ),
    ]
