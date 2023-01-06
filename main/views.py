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

def film_details(request, id):
    film_details = requests.get(f'https://api.themoviedb.org/3/movie/{id}?api_key={API_KEY_TMDB}').text
    film_details = json.loads(film_details)

    genres = []
    for genre in film_details.get('genres'):
        genres.append(genre.get('name'))

    data = {
        'original_title': film_details.get('original_title'),
        'overview': film_details.get('overview'),
        'origin_country': film_details.get('origin_country'),
        'genres': genres,
        'runtime': film_details.get('runtime'),
        'release_date': film_details.get('release_date')
    }

    return render(request, 'main/film_details.html', data)






