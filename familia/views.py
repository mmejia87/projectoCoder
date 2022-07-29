from django.shortcuts import render
from familia.models import Familiar


def hola(request):
    return render(request, 'miarchivo.html', context={})

def verFamiliar(request):

    familiar = Familiar(name="Homero",last_name="Simpson",edad="38",creation_date="1/2/22",email="homero@simpson.com")
    familiar = Familiar(name="Bart",last_name="Simpson",edad="9",creation_date="1/2/22",email="pequenodiablillo@simpson.com")
    familiar.save()

    familia=Familiar.objects.all()
    return render(request, "familiar.html", context={})