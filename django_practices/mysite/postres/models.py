from django.db import models

# Create your models here.

class Postre(models.Model):
    nombre = models.CharField(max_length=200)