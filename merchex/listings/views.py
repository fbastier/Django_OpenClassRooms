from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Title, Band
from listings.forms import ContactUsForm, BandForm, ListingForm
from django.core.mail import send_mail
from django.shortcuts import redirect


def band_list(request):
    bands = Band.objects.all()
    titles = Title.objects.all()
    return render(request, 'listings/band_list.html', context={'bands': bands})


def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html', context={'band': band})


def about(request):
    return render(request, 'listings/about.html')


def listings(request):
    titles = Title.objects.all()
    return render(request, 'listings/listings.html', context={'titles': titles})


def listings_detail(request, id):
    title = Title.objects.get(id=id)
    return render(request, 'listings/listings_detail.html', context={'title': title})


def listings_groupe(request, band):
    bands = Band.objects.get(id=band)
    titles = Title.objects.filter(band=band).values()
    return render(request, 'listings/listings_groupe.html', context={'titles': titles, 'band': bands})


def contact(request):
    print('la méthode de requête est : ', request.method)  # instructions impression dans terminal
    print('Les données POST sont : ', request.POST)
    if request.method == 'POST':
        form = ContactUsForm(request.POST)  # Créer instance formulaire remplie avec données POST
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via Merchex Contact Us',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz']
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()  # ajout d'un nouveau formulaire requête GET
    return render(request,
                  'listings/contact.html',
                  {'form': form})  # passe ce formulaire au gabarit


def mailSent(request):
    return render(request, 'listings/email-sent.html')


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request, 'listings/band_create.html', {'form': form})


def listing_create(request):
    if request.method == 'POST':
        title = ListingForm(request.POST)
        if title.is_valid():
            title = title.save()
            return redirect('merchandise_list')
    else:
        title = ListingForm()
    return render(request, 'listings/listing_create.html', {'title': title})


def band_update(request, id):
    band = Band.objects.get(id=id)
    if request.method == "POST":
        form = BandForm(request.POST, instance=band) # Pré-remplissage avec les datas d'un groupe existant
        if form.is_valid():
            form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)
    return render(request, 'listings/band_update.html', {'form': form})


def listing_update(request, id):
    title = Title.objects.get(id=id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=title)
        if form.is_valid:
            form.save()
            return redirect('merchandise_detail', title.id)
    else:
        form = ListingForm(instance = title)
    return render(request, 'listings/listing_update.html', {'form':form})


def band_delete(request, id):
    band = Band.objects.get(id=id) # pour GET et POST
    if request.method == "POST":
        band.delete()
        return redirect('band_list')
    # pas besoin de else, Si c'est une demande GET on continue
    return render(request, 'listings/band_delete.html', {'band': band})


def listing_delete(request, id):
    title = Title.objects.get(id=id) # pour GET et POST
    if request.method == "POST":
        title.delete()
        return redirect('merchandise_list')
    # pas besoin de else, Si c'est une demande GET on continue
    return render(request, 'listings/listing_delete.html', {'title': title})
