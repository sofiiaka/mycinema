from django.shortcuts import render, redirect
from .models import Film, Country, Genre
from .forms import FilmForm, FilmRemarksForm, FilmOwnRatingForm
from django.views.generic import DetailView, UpdateView, DeleteView
import requests
import json
from core.settings import API_KEY_TMDB
from django.urls import reverse_lazy


def home(request):
    founded_films = requests.get(
        f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY_TMDB}').text
    founded_films = json.loads(founded_films)


    data = {
        'founded_films': founded_films["results"]

    }
    return render(request, 'main/home.html', data)


def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            search_film = form.data.get('title')
            founded_films = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY_TMDB}&query={search_film}').text
            founded_films = json.loads(founded_films)

            data = []

            for founded_film in founded_films.get('results'):
                if Film.objects.filter(title=founded_film.get('title')).exists():
                    data.append({
                        'title': founded_film.get('title'),
                        'id': founded_film.get('id'),
                        'exists': True
                    })
                else:
                    data.append({
                        'title': founded_film.get('title'),
                        'id': founded_film.get('id'),
                        'exists': False
                    })

                results = {'data': data}
            return render(request, 'main/founded_films.html', results)
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
    film_images = requests.get(f'https://api.themoviedb.org/3/movie/{id}/images?api_key={API_KEY_TMDB}').text

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
        if film_details.get('production_countries'):
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
        else:
            country = None
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

def film_details_in_collection(request, id):
    form_remark = FilmRemarksForm()
    form_own_rating = FilmOwnRatingForm()
    film_details = Film.objects.get(id=id)
    data = {
        'title': film_details.title,
        'id': film_details.id,
        'overview': film_details.overview,
        'duration': film_details.duration,
        'year_production': film_details.year_production,
        'genre': film_details.genre_id.genre,
        'country_full_name': film_details.country_id.country_full_name,
        'country_short_name': film_details.country_id.country_short_name,
        'remark': film_details.remark,
        'own_rating': film_details.own_rating,
        'form_remark': form_remark,
        'form_own_rating': form_own_rating

    }
    if request.method == 'POST':
        form_remark = FilmRemarksForm(request.POST)
        form_own_rating = FilmOwnRatingForm(request.POST)
        if form_remark.is_valid():
            film_details.remark = form_remark.data.get('remark')
            film_details.save()
            data['remark'] = form_remark.data.get('remark')
        else:
            data['error'] ='Form is invalid'
        if form_own_rating.is_valid():
            film_details.own_rating = form_own_rating.data.get('own_rating')
            film_details.save()
            data['own_rating'] = form_own_rating.data.get('own_rating')
        else:
            data['error'] ='Form is invalid'
    return render(request, 'main/my_films_collection_details.html', data)


class FilmDeleteView(DeleteView):
    model = Film
    success_url = '/collections-film/'
    template_name = 'main/film_confirm_delete.html'
