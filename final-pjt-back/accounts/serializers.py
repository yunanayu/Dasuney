from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Actor, Director, Movie, Score


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','username',)

class LikeActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class LikeDirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class LikeMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'movie_id',)


class ScoreSerializer(serializers.ModelSerializer):
    movie = LikeMovieSerializer (read_only=True)
    class Meta:
        model = Score
        fields = '__all__'

class FollowSerializer(serializers.ModelSerializer):
    score_set = ScoreSerializer(many=True, read_only = True)
    like_actor = LikeActorSerializer(many = True, read_only = True)
    like_director = LikeDirectorSerializer(many = True, read_only = True)
    like_movies = LikeMovieSerializer(many = True, read_only = True)
    followers = UserSerializer(many=True, read_only=True)
    followings = UserSerializer(many=True, read_only=True)
    followers_count = serializers.IntegerField(source = 'followers.count', read_only = True)
    followings_count = serializers.IntegerField(source ='followings.count', read_only = True)
    class Meta:
        model = get_user_model()
        # include = ('id','username','followings','followers',)
        # fields = '__all__'
        exclude = ('password', 'last_login', 'is_superuser', 'first_name','last_name', 'email', 'is_staff', 'is_active', 'date_joined','groups','user_permissions',)