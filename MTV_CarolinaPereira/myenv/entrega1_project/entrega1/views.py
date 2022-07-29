from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def saludo(request):
    return HttpResponse("Esta es la entrega MTV 1 de Carolina Pereira")

def lista_familiares(request):
    today = datetime.now()
    context = {
        "name": "Pereira",
        "last_name": "Pereira",
        "age": 40,
        "relationship": "hermano",
        "sys_creation_date": today
        }
    return render(request, 'lista_familiares.html', context=context)

