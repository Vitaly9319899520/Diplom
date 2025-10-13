from django.shortcuts import render

from main.models import AboutPage


def index(request):
    return render(
        request,
        "main/index.html",
        context={
            "title": "Home-Главная",
            "content": 'Пекарня <br> В лаборатории у Бусинки',
        },
    )


def about(request):
    about_page = AboutPage.objects.first()
    return render(
        request,
        "main/about.html",
        context={
            "title": about_page.title,
            "content": about_page.content,
        },
    )
