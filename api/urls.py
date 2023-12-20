from django.urls import path
from .views import *

urlpatterns = [
    path('fluxentrants/create/', FluxEntrantsCreateView.as_view(), name='fluxentrants-create'),
    path('fluxentrants/list/', FluxEntrantsListView.as_view(), name='fluxentrants-list'),
    path('fluxentrants/bydate/', FluxEntrantsByDateView.as_view(), name='fluxentrants-bydate'),
]