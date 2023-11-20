from django.urls import path
from . import views
urlpatterns = [
    path('follow/<int:user_pk>/',views.follow ),
    path('profile/<str:username>/',views.profile ),
]
