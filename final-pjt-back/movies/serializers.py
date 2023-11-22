from rest_framework import serializers
from .models import Movie,Genre, Score, Actor, Director
from django.contrib.auth import get_user_model



class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'
        read_only_fields= ('movie', 'user',)

class MovieListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id','username',)
    score_set  = ScoreSerializer(many=True, read_only = True)
    like_users = UserSerializer(many=True)
    genres = GenreSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'


        
        

class ActorSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id','username',)
    
    like_users = UserSerializer(many=True)
    class Meta:
        model = Actor
        fields = '__all__'
        read_only_fields=('movie',)


class DirectorSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id','username',)
    
    like_users = UserSerializer(many=True)
    class Meta:
        model = Director
        fields ='__all__'