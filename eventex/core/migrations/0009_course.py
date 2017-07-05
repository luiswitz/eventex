# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 18:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20170705_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('talk_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Talk')),
                ('slots', models.IntegerField()),
            ],
            options={
                'verbose_name': 'curso',
                'verbose_name_plural': 'cursos',
            },
            bases=('core.talk',),
        ),
    ]