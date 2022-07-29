from unicodedata import name
from django.shortcuts import render
from familiares.models import Familiares

# Creo familiares

def create_family(request):
    new_family = Familiares.objects.create(name='Juan José', last_name='Pereira', age=40, relationship='hermano', sys_creation_date='2022-07-28')
    context = {
        'new_family': new_family
    }
    return render(request, "new_family.html", context=context)

def list_family(request):
    family = Familiares.objects.all()
    context = {
        'familia': family
    }
    return render(request, "list_family.html", context=context)
