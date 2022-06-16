from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Title, Band


def hello(request):
    bands = Band.objects.all()
    titles = Title.objects.all()
    return render(request, 'listings/hello.html', context={'bands':bands})


def about(request):
    return render(request, 'listings/about.html')


def listings(request):
    titles = Title.objects.all()
    return render(request, 'listings/listings.html', context={'titles':titles})


def contact(request):
    return render(request, 'listings/contact.html')
