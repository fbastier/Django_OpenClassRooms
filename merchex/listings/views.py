from django.http import HttpResponse
from listings.models import Band


def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Mes groupes :</p>
        <ul>
            <li>{bands[0].name} : {bands[0].title}</li>
            <li>{bands[1].name} : {bands[1].title}</li>
            <li>{bands[2].name} : {bands[2].title}</li>
        </ul>
""")


def about(request):
    return HttpResponse('<h1>A propos</h1><br><p>Nous sommes merchex</p>')


def listings(request):
    return HttpResponse('<h1>Liste des bidules</h1>')


def contact(request):
    return HttpResponse('<h1>Formulaire de contact</h1>')
