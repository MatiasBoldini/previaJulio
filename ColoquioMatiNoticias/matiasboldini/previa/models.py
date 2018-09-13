# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Noticia(models.Model):
        titulo = models.CharField(max_length=128)
        introduccion = models.CharField(max_length=300)
        descripcion = models.CharField(max_length=1000)
        image = models.ImageField()
        
class Puntaje(models.Model):
        user = models.ForeignKey(User)
        noticia = models.ForeignKey(Noticia)
        
        def promedio(self):
            suma= 0.0
            total = self.puntuaciones.count()
            for puntuacion in self.puntuaciones.all():
                suma += puntuacion.valor
            return float(suma)/total
            
class Puntuacion(models.Model):
        puntaje = models.ForeignKey(Puntaje, related_name='puntuaciones')
        valor =  models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])   