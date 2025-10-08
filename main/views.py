from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories

def index(request):

    categories = Categories.objects.all()
    return render(request, 'main/index.html', context={'title':'Home-Главная','content':'Магазин мебели HOME', 'categories': categories })

def about(request):
    return render(request, 'main/about.html', context={'title':'Home-О нас','content':'О нас', 'text_on_page':'Текст о магазине'})
