from django.shortcuts import render
from .models import Film
from .forms import FilmForm
from django.views.generic import DetailView, UpdateView, DeleteView
import imdb


ia = imdb.Cinemagoer()


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
            founded_films = ia.search_movie(search_film)
            #print(founded_films)
            #for founded_film in founded_films:
            #    print(founded_film.__dict__())
            data = {
                'founded_films': founded_films
            }
            return render(request, 'main/founded_films.html', data)
        else:
            error = 'Форма была неверной!'

    form = FilmForm()

    data = {
        'form': form
    }
    return render(request, 'main/add_film.html', data)




