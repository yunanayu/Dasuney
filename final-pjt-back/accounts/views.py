from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404,get_object_or_404
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserSerializer, FollowSerializer
# Create your views here.

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def profile(req, username):
    if req.method == 'GET':
        person = get_user_model().objects.get(username=username)
        serializer = FollowSerializer(person)
        return Response(serializer.data)
    elif req.method == 'POST':
        person = get_user_model().objects.get(username=username)
        print(req.user)
        if person != req.user:
            # if me in you.followers.all():
            if person.followers.filter(pk=req.user.pk).exists():
                person.followers.remove(req.user)
                if_followed = False
            else:
                person.followers.add(req.user)
                if_followed = True
            context = {
                'if_followed':if_followed,
                'followings_count' : person.followings.count(),
                'followers_count' : person.followers.count()
            }
        else:
            contest = {'err' : 'err'}
        return JsonResponse(context)
            
    


@api_view(['POST'])
def follow(req, user_pk):
    if req.method == 'POST':
        User = get_user_model()
        person = User.objects.get(pk=user_pk)
        print(person)
        if person != req.user:
            # if me in you.followers.all():
            if person.followers.filter(pk=req.user.pk).exists():
                person.followers.remove(req.user)
                if_followed = True
            else:
                person.followers.add(req.user)
                if_followed = False
            context = {
                'if_followed':if_followed,
                'followings_count' : person.followings.count(),
                'followers_count' : person.followers.count()
            }
        return JsonResponse(context)