from rest_framework import serializers
from .models import Review, Comment

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        # 시리얼라이저에 포함할 필드를 지정하세요

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # 시리얼라이저에 포함할 필드를 지정하세요
