from django.shortcuts import render
from fmembers.models import Fmembers

# Creo familiares

def create_fmember(request):
    new_fmember = Fmembers.objects.create(names='Juan José', last_name='Pereira', age=40, relationship='hermano', sys_creation_date='2022-07-28')
    context = {
        'new_fmember': new_fmember
    }
    return render(request, "new_fmember.html", context=context)

def list_fmembers(request):
    fmember = Fmembers.objects.all()
    context = {
        'fmember': fmember
    }
    return render(request, "list_fmembers.html", context=context)
