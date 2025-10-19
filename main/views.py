from django.shortcuts import render

from main.models import AboutPage, AboutDelivery, AboutContact


def index(request):
    return render(
        request,
        "main/index.html",
        context={
            "title": "Home-Главная",
            "content": "Пекарня <br> В лаборатории у Бусинки",
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

def delivery(request):
        about_delivery = AboutDelivery.objects.first()
        return render(
            request,
            "main/delivery.html",
            context={
                "title": about_delivery.title,
                "content": about_delivery.content,
            },
        )


def contact(request):
    about_contact = AboutContact.objects.first()
    return render(
        request,
        "main/contact.html",
        context={
            "title": "",
            "content": "Мы находимся по адресу: СПб, Площадь Конституции, к.1 <br> Телефон для связи: <br> +7 931 989 95 20",
        },
    )
