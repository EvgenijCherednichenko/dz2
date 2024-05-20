from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, hom

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', hom, name='contacts')
]
