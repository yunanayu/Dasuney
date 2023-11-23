from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Review, Comment
from .serializers import ReviewSerializer, CommentSerializer
from  rest_framework import status
from movies.models import Movie


# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
def review_list(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        # 모든 리뷰 뽑기
        # reviews = get_list_or_404(Review)
        # 해당 영화의 리뷰 리스트를 뽑아오기?---x
        reviews = movie.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=204)

@api_view(['GET', 'POST'])
def comment_list(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        # comments = review.comments.all()
        comments = review.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, user=request.user)
            return Response(serializer.data, status=201)
        # return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        if request.user.pk == comment.user.id:
            serializer = CommentSerializer(comment, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        if request.user.pk == comment.user.id:
            comment.delete()
            return Response(status=204)



@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def review_likes(req, review_pk):
    if req.method == 'GET':
        review = get_object_or_404(Review, pk=review_pk)
        if req.user in review.user_likes.all():
            is_liked = True
        else:
            is_liked = False
        context = {
            'is_liked' : is_liked,
            'like_count' : review.user_likes.count()
        }
        return JsonResponse(context)
    elif req.method == 'POST':
        review = get_object_or_404(Review, pk=review_pk)
        if req.user.pk != review.user.id:
            if req.user in review.user_likes.all():
                review.user_likes.remove(req.user)
                is_liked = False
            else:
                review.user_likes.add(req.user)
                is_liked = True
            context = {
                'is_liked' : is_liked,
                'like_count' : review.user_likes.count()
            }
            return JsonResponse(context)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
