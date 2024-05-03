# No arquivo urls.py dentro do aplicativo 'profiles'

from atexit import register
from django import views
from django.urls import path
from .views import profile_view, swipe_view
from .views import profile_update

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('swipe/<int:profile_id>/', swipe_view, name='swipe'),
    path('register/', register, name='register'),
    path('accounts/profile/', profile_view, name='profile'),
    path('profile/update/', profile_update, name='profile_update'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('create_profile/', views.create_profile, name='create_profile'),

    
]
