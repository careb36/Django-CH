from django.contrib import admin
from django.urls import path
from fmembers.views import list_fmembers, create_fmember

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list_fmembers/', list_fmembers, name='list_fmembers'),
    path('create_fmember/', create_fmember, name='create_fmember'),
]
    