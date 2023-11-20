from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/movielike/', views.movie_likes),
    path('<int:movie_pk>/score/', views.score_create),
    path('<int:movie_pk>/score/<int:score_pk>/', views.score_update),
    path('<int:movie_pk>/actor/', views.actor_add),
    path('<int:movie_pk>/actor/<int:actor_pk>/', views.actor_update),
    path('<int:movie_pk>/director/', views.director_add),
    path('<int:movie_pk>/director/<int:director_pk>/', views.director_update),
    path('actor/<int:actor_pk>/actorlike/', views.actor_likes),
    path('director/<int:director_pk>/', views.director_likes),
    path('actors/', views.actor_list),
]
