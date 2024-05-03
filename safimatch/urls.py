from django.contrib import admin
from django.urls import path
from profiles.views import profile_view, swipe_view
from django.contrib.auth.views import LoginView  # Importe a view padrão de login
from profiles.views import register, profile_update


urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', profile_view, name='profile'),
    path('swipe/<int:profile_id>/', swipe_view, name='swipe'),
    path('accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', register, name='register'),
    path('profile/update/', profile_update, name='profile_update'),
    path('', profile_view, name='home'),
    path('accounts/profile/', profile_view, name='profile'),
    path('profile/update/', profile_update, name='profile_update'),
]

