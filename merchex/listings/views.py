from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band


def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', context={'bands':bands})


def about(request):
    return render(request, 'listings/about.html')


def listings(request):
    titles = Band.objects.all()
    return render(request, 'listings/listings.html', context={'titles':titles})


def contact(request):
    return render(request, 'listings/contact.html')
