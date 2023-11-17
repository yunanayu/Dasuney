from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.movie_list),
    path('detail/<int:movie_pk>/', views.movie_detail),
    path('movielike/<int:movie_pk>', views.movie_likes),
    path('score/', views.score),
    path('actor/', views.actor),
]
