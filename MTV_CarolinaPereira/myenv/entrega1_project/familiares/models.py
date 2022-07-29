from unicodedata import name
from django.db import models

class Familiares(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    relationship = models.CharField(max_length=40)
    sys_creation_date = models.DateTimeField(auto_now_add=True)
