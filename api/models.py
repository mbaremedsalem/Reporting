from django.db import models

# Create your models here.
TypeSwfit=(
    ('MT103','MT103'),
    ('MT754', 'MT754'),
)  

ModeReglement=(
    ('TL','TL'),
    ('CD','CD'),
    ('RD','RD')
)
Devise = (
    ('EUR','EUR'),
    ('USD','USD')
)

class FluxEntrants(models.Model):
    Banque = models.CharField(max_length=200)
    eferenceTransaction = models.CharField(max_length=200)
    dateTransaction = models.DateField(auto_now_add=True)
    typeSwfit = models.CharField(max_length=30, choices=TypeSwfit,null=True,default='MT103')
    modeReglement = models.CharField(max_length=3, choices=ModeReglement,null=True,default='TL')
    devise = models.CharField(max_length=5,choices=Devise,null=True,default='EUR')
    montantTransaction = models.FloatField(max_length=255, default=0.0)
    tauxDeChange = models.FloatField(max_length=255, default=0.0)
    nomDonneurOrdre = models.CharField(max_length=255)
    nif_nni = models.CharField(max_length= 200)
    beneficiaire = models.CharField(max_length=100)
    produit = models.CharField(max_length=200)
    natureEconomique = models.CharField(max_length=200)
    pays = models.CharField(max_length=200)
