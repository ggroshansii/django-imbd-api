from django.shortcuts import render
from watchlist.models import Movie

# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    print(movies)