# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-13 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_auto_20160627_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='url_title',
            field=models.CharField(max_length=255, unique=True, verbose_name='url_title'),
        ),
    ]
