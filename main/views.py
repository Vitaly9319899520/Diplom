from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html', context={'title':'Home','content':'Главная страница' })

def about(request):
    return HttpResponse('About page')
