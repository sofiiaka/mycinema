from django.shortcuts import render
from .models import Film

def home(request):
    return render(request, 'main/home.html')

def my_films(request):
    film = Film.objects.order_by('-year_prodaction_id')
    return render(request, 'main/my_films.html', {'film': film})
