from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('movielike/<int:movie_pk>/', views.movie_likes),
    path('<int:movie_pk>/score/', views.score_create),
    path('<int:movie_pk>/score/<int:score_pk>/', views.score_update),
    path('actor/', views.actor),
]
