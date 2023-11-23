from django.urls import path
from . import views
urlpatterns = [
    # path('follow/<int:user_pk>/',views.follow ),
    path('profile/<str:username>/',views.profile ), # 프로필로 이동, 팔로우 기능
    path('profile/<str:username>/picture/', views.upload_picture),
]
