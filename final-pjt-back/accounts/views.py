from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404,get_object_or_404
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['POST'])
def profile(req, username):
    if req.method == 'POST':
        User = get_user_model()
        person = User.objects.get(username=username)
        context = {
            'person' : person
        }
        return JsonResponse(context)

@api_view(['POST'])
def follow(req, user_pk):
    if req.method == 'POST':
        User = get_user_model()
        person = User.objects.get(pk=user_pk)
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