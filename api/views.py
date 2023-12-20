from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FluxEntrants
from .serializers import FluxEntrantsSerializer


class FluxEntrantsCreateView(generics.CreateAPIView):
    queryset = FluxEntrants.objects.all()
    serializer_class = FluxEntrantsSerializer

class FluxEntrantsListView(generics.ListAPIView):
    queryset = FluxEntrants.objects.all()
    serializer_class = FluxEntrantsSerializer

class FluxEntrantsByDateView(APIView):
    def post(self, request, format=None):
        date_transaction = request.data.get('dateTransaction', None)
        if date_transaction:
            fluxentrants = FluxEntrants.objects.filter(dateTransaction=date_transaction)
            serializer = FluxEntrantsSerializer(fluxentrants, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "Veuillez fournir une date de transaction dans le corps de la requête."}, status=400)