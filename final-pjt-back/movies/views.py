from django.shortcuts import render
from django.shortcuts import get_list_or_404,get_object_or_404
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.db.models import Sum, Avg
from rest_framework import status
from .models import Movie,Genre, Score, Actor, Director
from .serializers import MovieListSerializer, GenreSerializer, MovieListSerializer,ScoreSerializer,ActorSerializer,DirectorSerializer
from django.contrib.auth import get_user_model
# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
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


@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def movie_likes(req, movie_pk):
    if req.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        if req.user in movie.like_users.all():
            is_liked = True
        else:
            is_liked = False
        context = {
            'is_liked' : is_liked,
        }
        return JsonResponse(context)
    elif req.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
        if req.user in movie.like_users.all():
            movie.like_users.remove(req.user)
            is_liked = False
        else:
            movie.like_users.add(req.user)
            is_liked = True
        context = {
            'is_liked' : is_liked,
            'like_count' : movie.like_users.count()
        }
        return JsonResponse(context)



@api_view(['GET','POST', 'PUT', 'DELETE'])
def score_create(req, movie_pk):
    # if req.method == 'GET':
    #     movie = get_object_or_404(Movie, pk=movie_pk)
        
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
            serializer.save()
            return Response(serializer.data)
    elif req.method == 'DELETE':
        score = get_object_or_404(Score, pk= score_pk)
        score.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET','POST'])
def actor_list(req):
    if req.method == 'GET':
        actors = get_list_or_404(Actor)
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)

@api_view(['GET','POST'])
def director_list(req):
    if req.method == 'GET':
        directors = get_list_or_404(Director)
        serializer = DirectorSerializer(directors, many=True)
        return Response(serializer.data)


@api_view(['GET','POST'])
def actor_add(req, movie_pk):
    if req.method == 'POST':
        movie = get_object_or_404(Movie, pk= movie_pk)
        serializer = ActorSerializer(data=req.data)
        if serializer.is_valid(raise_exception=True):           
            serializer.save()
            return Response(serializer.data)
    elif req.method == 'GET':
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)
        
@api_view(['PUT', 'DELETE'])     
def actor_update(req, movie_pk, actor_pk):
    if req.method == 'PUT':
        movie = get_object_or_404(Movie, pk= movie_pk)
        actor = get_object_or_404(Actor, pk=actor_pk)
        serializer = ActorSerializer(actor, data=req.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data)
    elif req.method == 'DELETE':
        actor = get_object_or_404(Actor, pk=actor_pk)
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
@api_view(['GET','POST'])
def director_add(req, movie_pk):
    if req.method == 'GET':
        directors = get_list_or_404(Director)
        serializer = DirectorSerializer(directors)
        return Response(serializer.data)
    elif req.method == 'POST':
        movie = get_object_or_404(Movie, pk= movie_pk)
        serializer = DirectorSerializer(data=req.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # movie.movie.add(req.data.m)
            # serializer.save(movie=movie)
            return Response(serializer.data)
        
        
@api_view(['GET','PUT', 'DELETE'])     
def director_update(req, movie_pk, director_pk):
    if req.method == 'GET':
        director = get_object_or_404(Director, pk=director_pk)
        serializer = DirectorSerializer(director)
        return Response(serializer.data)
    elif req.method == 'PUT':
        movie = get_object_or_404(Movie, pk= movie_pk)
        director = get_object_or_404(Actor, pk=director_pk)
        serializer = DirectorSerializer(director, data=req.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data)
    elif req.method == 'DELETE':
        director = get_object_or_404(Actor, pk=director_pk)
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def actor_likes(req, actor_pk):
    if req.method == 'GET':
        actor = get_object_or_404(Actor, pk=actor_pk)
        if req.user in actor.like_users.all():
            is_liked = True
        else:
            is_liked = False
        context = {
            'is_liked' : is_liked,
        }
        return JsonResponse(context)
    elif req.method == 'POST':
        actor = get_object_or_404(Actor, pk=actor_pk)
        if req.user in actor.like_users.all():
            actor.like_users.remove(req.user)
            is_liked = False
        else:
            actor.like_users.add(req.user)
            is_liked = True
        context = {
            'is_liked' : is_liked,
            'like_count' : actor.like_users.count()
        }
        return JsonResponse(context)
    

@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def director_likes(req, director_pk):
    if req.method == 'GET':
        director = get_object_or_404(Director, pk=director_pk)
        if req.user in director.like_users.all():
            is_liked = True
        else:
            is_liked = False
        context = {
            'is_liked' : is_liked,
            'like_count' : director.like_users.count()
        }
        return JsonResponse(context)
    elif req.method == 'POST':
        director = get_object_or_404(Director, pk=director_pk)
        if req.user in director.like_users.all():
            director.like_users.remove(req.user)
            is_liked = False
        else:
            director.like_users.add(req.user)
            is_liked = True
        context = {
            'is_liked' : is_liked,
            'like_count' : director.like_users.count()
        }
        return JsonResponse(context)
    
    
    
# 리뷰와 좋아요(보고싶어요) 기반으로 영화 추천
@api_view(['GET'])
def recommend_by_review(req):
    user = req.user
    reviews = user.review_set.all()
    likes = user.like_movies.all()
    
    if not reviews and not likes:
        return Response([], status=status.HTTP_200_OK)

    genres = {
        '액션': {'score': 0, 'count': 0},
        "모험": {'score': 0, 'count': 0},
        "애니메이션": {'score': 0, 'count': 0},
        "코미디": {'score': 0, 'count': 0},
        "범죄": {'score': 0, 'count': 0},
        "다큐멘터리": {'score': 0, 'count': 0},
        "드라마": {'score': 0, 'count': 0},
        "가족": {'score': 0, 'count': 0},
        "판타지": {'score': 0, 'count': 0},
        "역사": {'score': 0, 'count': 0},
        "공포": {'score': 0, 'count': 0},
        "음악": {'score': 0, 'count': 0},
        "미스터리": {'score': 0, 'count': 0},
        "로맨스": {'score': 0, 'count': 0},
        "SF": {'score': 0, 'count': 0},
        "TV 영화": {'score': 0, 'count': 0},
        "스릴러": {'score': 0, 'count': 0},
        "전쟁": {'score': 0, 'count': 0},
        "서부": {'score': 0, 'count': 0},
    }

# 모든 점수를 합산하는 경우
        # total_score = review.movie.score_set.all().aggregate(Sum('score'))['score__sum']

        # 또는 평균을 계산하는 경우
        # average_score = review.movie.score_set.all().aggregate(Avg('score'))['score__avg']

# 그리고 이 값을 int로 변환하여 사용하면 됩니다.
        # if total_score is not None:
        #     genres[genre.name]['score'] += int(total_score)
            

    # review_movies = []
    # for review in reviews:
    #     review_movies.append(review.movie.title)
    #     for genre in review.movie.genres.all():
    #         genres[genre.name]['score'] += int(review.movie.score_set.all())
    #         genres[genre.name]['count'] += 1
            
    review_movies = []
    for review in reviews:
        review_movies.append(review.movie.title)
        total_score = review.movie.score_set.all().aggregate(Sum('score'))['score__sum']
        for genre in review.movie.genres.all():
            if total_score is not None:
                genres[genre.name]['score'] += int(total_score)
            genres[genre.name]['count'] += 1
                        
            
            
    for like in likes:
        if like.title not in review_movies:
            for genre in like.genres.all():
                genres[genre.name]['score'] += 7
                genres[genre.name]['count'] += 1
                
                
    for genre, data in genres.items():
        if data['count'] > 0:
            data['avg'] = round(data['score'] / data['count'], 1)
        else:
            data['avg'] = 0
            
    def sorting_algorithm(movie):
        movie_score = 0
        movie_genres = movie.genres.all()
        for movie_genre in movie_genres:
            movie_score += genres[movie_genre.name]['avg']
        movie_score = round(movie_score / len(movie_genres), 1)
        return (-movie_score, -movie.vote_average, -movie.vote_count)

    movies = Movie.objects.order_by('-popularity', '-release_date')[:500]
    movies = sorted(movies,
                    key=sorting_algorithm)

    def make_recommend_movies():
        recommend_movies = []
        for movie in movies:
            if movie not in likes and movie not in reviews:
                recommend_movies.append(movie)
                if len(recommend_movies) >= 30:
                    return recommend_movies
        return recommend_movies

    recommend_movies = make_recommend_movies()
    serializer = MovieListSerializer(recommend_movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



# 비슷한 취향을 가진 사람들이 본 영화
# 좋아요 유사 사용자 추천 알고리즘으로 추천된 영화 리스트

@api_view(['GET'])
def recommend_by_users(request):
    me = request.user
    me_like_movies = me.like_movies.all()

    if len(me_like_movies) == 0:
        return Response([], status=status.HTTP_200_OK)

    users = get_user_model().objects.all()

    similar_users = sorted(users, key=lambda user: len(
        set(user.like_movies.all()).intersection(me_like_movies)))

    def make_recommend_movies():
        recommend_movies = set()
        for similar_user in similar_users:
            for like_movie in similar_user.like_movies.all():
                if like_movie not in me_like_movies:
                    recommend_movies.add(like_movie)
                    if len(recommend_movies) >= 30:
                        return recommend_movies
        return list(recommend_movies)

    recommend_movies = make_recommend_movies()

    serializer = MovieListSerializer(recommend_movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
