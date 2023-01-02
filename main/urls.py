from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('myfilms', views.my_films),
    path('add_film', views.add_film, name='add_film')
]