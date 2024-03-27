from django.db import models

# Create your models here.
import requests
from django.db import models

# Modèle pour stocker les données des comptes Snapchat
class CompteSnapchat(models.Model):
    nom_compte = models.CharField(max_length=100)
    description = models.TextField()
    followers = models.IntegerField()

    def __str__(self):
        return self.nom_compte

