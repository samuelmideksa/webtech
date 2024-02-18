from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

def home(request):
    albums = Album.objects.all()
    data = {
        'albums': albums
    }

    return render(request, 'home.html', data)


def about(request):
    return HttpResponse('about page')


def contact_page(request):
    return HttpResponse('contact page')


def music(request):
    return HttpResponse('music page')

