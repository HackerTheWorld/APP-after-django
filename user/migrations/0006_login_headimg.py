# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 05:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20171106_0231'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='headimg',
            field=models.FileField(null=True, upload_to='./uploadhead'),
        ),
    ]