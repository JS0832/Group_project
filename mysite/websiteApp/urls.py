from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('game/', views.game, name='game'),
    path('main/', views.main, name='main'),
    path('location/', views.location, name='location'),
    path('campus_exploration/', views.campus_exploration, name='campus_exploration'),
    path('settings/', views.settings, name='settings'),
    path('introduce/', views.introduce, name='introduce')
]
