from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-film', views.add_film, name='add_film'),
    path('film/<id>',  views.film_details, name='film_detail'),
    path('add-film-to-collection/<id>', views.add_film_to_collection, name='add_film_to_collection'),
    path('collections-film/', views.collections_film, name='collections_film'),
    path('film-already-exist-error/', views.film_already_exist, name='film_already_exist_error'),
    path('film-details-in-collection/<id>',views.film_details_in_collection, name='film_details_in_collection' )
]