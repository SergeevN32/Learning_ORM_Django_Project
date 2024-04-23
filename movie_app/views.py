from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
from .models import Movie, Director, Actor
from django.views.generic import ListView, DetailView


# Create your views here.

def show_all_movie(request):
    # movies = Movie.objects.order_by(F('year').desc(nulls_last=True), 'rating')
    movies = Movie.objects.annotate(
        true_bool=Value(True),
        false_bool=Value(False),
        str_field=Value('hello'),
        new_budget=F('budget') + 100,
        ffff=F('rating') * F('year'),
    )
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('id'))
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg': agg,
    })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {'movie': movie, })


class ListAllDirectors(ListView):
    template_name = 'movie_app/all_directors.html'
    model = Director
    context_object_name = 'directors'


class ListAllActors(ListView):
    template_name = 'movie_app/all_actors.html'
    model = Actor
    context_object_name = 'actors'


# def show_all_directors(request):
#     directors = Director.objects.all()
#     return render(request, 'movie_app/all_directors.html', {'directors': directors, })


class DetailOneDirector(DetailView):
    template_name = 'movie_app/one_director.html'
    model = Director
    context_object_name = 'director'


# def show_one_director(request, id: int):
#     director = get_object_or_404(Director, id=id)
#     return render(request, 'movie_app/one_director.html', {'director': director, })


# def show_all_actors(request):
#     actors = Actor.objects.all()
#     return render(request, 'movie_app/all_actors.html', {'actors': actors, })


class DetailOneActor(DetailView):
    template_name = 'movie_app/one_actor.html'
    model = Actor
    context_object_name = 'actor'


def show_one_actor(request, slug_actor: str):
    actor = get_object_or_404(Actor, slug=slug_actor)
    return render(request, 'movie_app/one_actor.html', {'actor': actor, })
