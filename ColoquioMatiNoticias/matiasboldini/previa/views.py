# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import *
# Create your views here.

def home(request):
    context = {}
    context['noticias'] = Noticia.objects.all()
    context['puntajes'] = Puntaje.objects.all()
    context['puntuacions'] = Puntuacion.objects.all()
    
    return render(request, 'home.html', context)