from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('myfilms', views.my_films)
]