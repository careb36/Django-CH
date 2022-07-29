from django.shortcuts import render
from fmembers.models import Fmembers

# Creo familiares

def create_fmember(request):
    new_fmember = Fmembers.objects.create(names='María Ivonne', last_name='Palomeque', age=40, relationship='madre', sys_creation_date='2022-07-28')
    context = {
        'new_fmember': new_fmember
    }
    return render(request, "new_fmember.html", context=context)

def list_fmembers(request):
    fmember = Fmembers.objects.all()
    context = {
        'fmember': fmember
    }
    return render(request, "fmembers_list.html", context=context)
