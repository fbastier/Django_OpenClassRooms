from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Title, Band


def band_list(request):
    bands = Band.objects.all()
    titles = Title.objects.all()
    return render(request, 'listings/band_list.html', context={'bands':bands})

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html', context={'band':band})


def about(request):
    return render(request, 'listings/about.html')


def listings(request):
    titles = Title.objects.all()
    return render(request, 'listings/listings.html', context={'titles':titles})


def listings_detail(request, id):
    title = Title.objects.get(id=id)
    return render(request, 'listings/listings_detail.html', context={'title':title})

def listings_groupe(request, band):
    title = Title.objects.get(band=band)
    return render(request, 'listings/listings_groupe.html', context={'band':band, 'title':title})


def contact(request):
    return render(request, 'listings/contact.html')
