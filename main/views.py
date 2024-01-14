from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'Головна SoftAndWood',
        'content': 'Головна сторінка магазина - SoftAndWood',
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'SoftAndWood - Про нас',
        'content': 'Про нас',
        'text_on_page': "текст про нас і чому ми найкращі.",
    }

    return render(request, 'main/about.html', context)
