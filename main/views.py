from django.shortcuts import render
from .models import Film
from .forms import FilmForm
from django.views.generic import DetailView, UpdateView, DeleteView

def home(request):
    return render(request, 'main/home.html')

def my_films(request):
    film = Film.objects.order_by('-year_prodaction_id')
    return render(request, 'main/my_films.html', {'film': film})

def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной!'

    form = FilmForm()

    data = {
        'form': form
    }
    return render(request, 'main/add_film.html', data)