# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-04 16:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('previa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='puntuacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='previa.Puntaje'),
            preserve_default=False,
        ),
    ]
