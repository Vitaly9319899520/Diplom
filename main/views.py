from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html', context={'title':'Home-Главная','content':'Магазин мебели HOME'})

def about(request):
    return render(request, 'main/about.html', context={'title': 'Home-О нас','content': 'О нас', 'text_on_page': 'Текст о магазине'})

