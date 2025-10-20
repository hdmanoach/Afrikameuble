from django.db import models

# Create your models here.
from django.db import models

class Meuble(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='meubles/')  

    def __str__(self):
        return self.nom

class Register(models.Model):
    username = models.CharField(max_length=100, unique=True) 
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__ (self):
        return self.username
    