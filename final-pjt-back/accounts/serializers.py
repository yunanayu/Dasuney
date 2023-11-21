from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','username',)
        
class FollowSerializer(serializers.ModelSerializer):
    followers = UserSerializer(many=True, read_only=True)
    followings = UserSerializer(many=True, read_only=True)
    followers_count = serializers.IntegerField(source = 'followers.count', read_only = True)
    followings_count = serializers.IntegerField(source ='followings.count', read_only = True)
    class Meta:
        model = get_user_model()
        # include = ('id','username','followings','followers',)
        # fields = '__all__'
        exclude = ('password', 'last_login', 'is_superuser', 'first_name','last_name', 'email', 'is_staff', 'is_active', 'date_joined','groups','user_permissions',)