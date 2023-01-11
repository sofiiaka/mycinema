from django.shortcuts import render, redirect
from .models import Film, Country, Genre
from .forms import FilmForm
from django.views.generic import DetailView, UpdateView, DeleteView
import requests
import json
from core.settings import API_KEY_TMDB

def home(request):
    return render(request, 'main/home.html')


def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            search_film = form.data.get('title')
            founded_films = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY_TMDB}&query={search_film}').text
            founded_films = json.loads(founded_films)

            data = {
                'founded_films': founded_films["results"]

            }
            return render(request, 'main/founded_films.html', data)
        else:
            error = 'The form was incorrect!'

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
        'id': film_details.get('id'),
        'overview': film_details.get('overview'),
        'production_countries': film_details.get('production_countries'),
        'genres': genres,
        'runtime': film_details.get('runtime'),
        'release_date': film_details.get('release_date')
    }

    return render(request, 'main/film_details.html', data)


def add_film_to_collection(request, id):
    film_details = requests.get(f'https://api.themoviedb.org/3/movie/{id}?api_key={API_KEY_TMDB}').text
    film_details = json.loads(film_details)
    film_already_exist = Film.objects.filter(title=film_details.get('title')).exists()
    if film_already_exist:
        return redirect('/film-already-exist-error/')
    else:
        for production_country in film_details.get('production_countries'):
            if production_country.get('iso_3166_1') and production_country.get('name'):
                try:
                    country = Country.objects.get(country_short_name=film_details.get('iso_3166_1'), country_full_name=film_details.get('name'))
                    production_country_id = country.id
                except Exception:
                    country = Country(
                        country_short_name=production_country.get('iso_3166_1'),
                        country_full_name=production_country.get('name')
                    )
                    country.save()
                    production_country_id = country.id
        for genres in film_details.get('genres'):
            if genres.get('id') and genres.get('name'):
                try:
                    genre = Genre.objects.get(id=film_details.get('id'), genre=film_details.get('name'))
                    genre_id = genre.id
                except Exception:
                    genre = Genre(
                        id=genres.get('id'),
                        genre=genres.get('name')
                    )
                    genre.save()
                    genre_id = genre.id

        film = Film(
            title=film_details.get('original_title'),
            overview=film_details.get('overview'),
            duration=film_details.get('runtime'),
            year_production=film_details.get('release_date'),
            genre_id=genre,
            country_id=country
        )
        film.save()
        return redirect('/collections-film/')


def collections_film(request):
    films = Film.objects.all()
    data = {
        'films': films
    }
    return render(request, 'main/my_films_collection.html', data)


def film_already_exist(request):
    return render(request, 'main/film_already_exist_error.html')