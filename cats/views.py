from django.shortcuts import render
from .models import Item

# Create your views here.


def main_page(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'cats/index.html', context)


def sign_up(request):
    return render(request, 'cats/sign_up.html')
    