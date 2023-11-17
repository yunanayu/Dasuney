from django.shortcuts import render
from django.shortcuts import get_list_or_404,get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Movie,Genre, Score, Actor, Director
from .serializers import MovieListSerializer


# Create your views here.
@api_view(['GET'])
def movie_list(req):
    if req.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movie_detail(req, movie_pk):
    if req.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieListSerializer(movie)
        return Response(serializer.data)

@api_view(['GET'])
def movie_likes(req, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if req.user in movie.movie_like.all():
        movie.movie_like.all.remove(req.user)
    else:
        movie.movie_like.all.add(req.user)

        
def score(req):
    pass

def actor(req):
    pass