# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20171115_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toutiao',
            name='media_name',
            field=models.TextField(verbose_name='作者昵称'),
        ),
        migrations.AlterField(
            model_name='toutiao',
            name='title',
            field=models.TextField(verbose_name='标题'),
        ),
    ]
