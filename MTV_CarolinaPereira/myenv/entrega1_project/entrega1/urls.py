from django.contrib import admin
from django.urls import path
from entrega1.views import saludo, lista_familiares
from familiares.views import new_family, list_family

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('lista_familiares/', lista_familiares, name='lista_familiares'),
    path('new_family/', new_family, name='new_family'),
    path('list_family/', list_family, name='list_family'),
]
    