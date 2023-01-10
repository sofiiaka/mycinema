from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add-film', views.add_film, name='add_film'),
    path('film/<id>',  views.film_details, name='film_detail'),
    path('add-film-to-collection/<id>', views.add_film_to_collection, name='add_film_to_collection'),
    path('collections-film/', views.collections_film, name='collections_film')
]