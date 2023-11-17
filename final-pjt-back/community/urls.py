# community/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.review_list),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('reviews/<int:review_pk>/comments/', views.comment_list),
    path('reviews/<int:review_pk>/comments/<int:comment_pk>/', views.comment_detail),
]
