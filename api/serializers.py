from rest_framework import serializers
from .models import FluxEntrants

class FluxEntrantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FluxEntrants
        fields = '__all__'
       

               # ('Banque','eferenceTransaction','typeSwfit','modeReglement','devise','montantTransaction','tauxDeChange','nomDonneurOrdre','nif_nni','beneficiaire','produit','natureEconomique','pays')  
       


#        {
#     "Banque":"AUB",
#     "eferenceTransaction":"AB123456789",
#     "typeSwfit":"MT103",
#     "modeReglement":"TL",
#     "devise":"EUR",
#     "montantTransaction":100000,
#     "tauxDeChange":39.5,
#     "nomDonneurOrdre":"AGENCE ADB",
#     "nif_nni":"1234567890",
#     "beneficiaire":"MED",
#     "produit":"poisson congelé",
#     "natureEconomique":"TOURISMES",
#     "pays":"Maroc"
# }