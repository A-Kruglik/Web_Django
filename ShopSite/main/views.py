from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from .models import *




def index(request):
    posts = Main.objects.all()
    return render(request, 'main/index.html', {'posts': posts, })


def about(request):
    return render(request, 'main/about.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')