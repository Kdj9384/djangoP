# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
