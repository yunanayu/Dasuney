from django.shortcuts import render
from django.shortcuts import get_list_or_404,get_object_or_404
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Movie,Genre, Score, Actor, Director
from .serializers import MovieListSerializer, GenreSerializer, MovieListSerializer,ScoreSerializer,ActorSerializer,DirectorSerializer

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


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
    if req.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
        if req.user in movie.movie_like.all():
            movie.movie_like.all.remove(req.user)
            is_liked = False
        else:
            movie.movie_like.all.add(req.user)
            is_liked = True
        context = {
            'movie_like' : movie.movie_like.all(),
            'is_liked' : is_liked,
            'like_count' : movie.movie_like.count()
        }
        return JsonResponse(context)

@api_view(['POST', 'PUT', 'DELETE'])
def score_create(req, movie_pk):
    if req.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = ScoreSerializer(data = req.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=req.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST', 'PUT', 'DELETE'])
def score_update(req, movie_pk, score_pk):
    if req.method == 'PUT':
        score = get_object_or_404(Score, pk= score_pk)
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = ScoreSerializer(score, data=req.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=req.user, movie=movie)
            return Response(serializer.data)
    elif req.method == 'DELETE':
        score = get_object_or_404(Score, pk= score_pk)
        score.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


@api_view(['POST', 'PUT', 'DELETE'])
def actor(req):
    if req.method == 'POST':
        serializer = ActorSerializer(data=req.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()