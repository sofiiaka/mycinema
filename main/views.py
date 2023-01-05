from django.shortcuts import render
from .models import Film
from .forms import FilmForm
from django.views.generic import DetailView, UpdateView, DeleteView
import requests
import json
from core.settings import API_KEY_TMDB

def home(request):
    return render(request, 'main/home.html')

def my_films(request):
    film = Film.objects.order_by('-year_prodaction_id')
    return render(request, 'main/my_films.html', {'film': film})

def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            search_film = form.data.get('ukrainian_full_name')
            founded_films = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY_TMDB}&query={search_film}').text
            founded_films = json.loads(founded_films)

            #print(type(founded_films))


            data = {
                'founded_films': founded_films["results"]

            }
            return render(request, 'main/founded_films.html', data)
        else:
            error = 'Форма была неверной!'

    form = FilmForm()

    data = {
        'form': form
    }
    return render(request, 'main/add_film.html', data)

def film_detail(request, movieID):
    film_detail = ia.get_movie(movieID)
    print(type(film_detail))
    print(film_detail.genres)
    return render(request, 'main/add_film.html')



