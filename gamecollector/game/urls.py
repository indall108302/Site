from django.urls import path

from . import views

urlpatterns = [
    path('', views.GameHome.as_view(), name='home'),
    path('genre/<slug:genre_slug>/', views.genre, name='genre'),
    path('add_game/', views.AddGame.as_view(), name='add_game'),
    path('game/<slug:game_slug>/', views.game_show, name='game'),
]

