# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-25 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datanalyse', '0009_delete_tickercomp'),
    ]

    operations = [
        migrations.CreateModel(
            name='TickerComp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=2000)),
                ('name', models.CharField(max_length=2000)),
            ],
        ),
    ]