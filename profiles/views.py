# No arquivo views.py dentro do aplicativo 'profiles'

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .utils import find_matches
from .models import Profile, Swipe
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, ProfileUpdateForm
from .forms import ProfileForm
from django.contrib import messages

@login_required
def profile_view(request):
    # Obtém o perfil do usuário logado
    profile = request.user.profile
    # Obtém perfis de outros usuários (exceto o próprio usuário)
    other_profiles = Profile.objects.exclude(user=request.user)
    return render(request, 'profile.html', {'profile': profile, 'other_profiles': other_profiles})

@login_required
def swipe_view(request, profile_id):
    # Obtém o perfil do usuário que está sendo "swiped"
    swiped_profile = Profile.objects.get(pk=profile_id)
    if request.method == 'POST':
        like = request.POST.get('like') == 'true'  # Obtém a escolha do usuário (like/dislike)
        Swipe.objects.create(swiper=request.user, swiped=swiped_profile.user, like=like)
        # Lógica para verificar se houve correspondência e atualizar os modelos, se necessário
        return redirect('profile')  # Redireciona de volta para a página de perfil
    else:
        return render(request, 'swipe.html', {'swiped_profile': swiped_profile})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Criar um perfil para o usuário
            Profile.objects.create(user=user)
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile_update(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'profile_update.html', {'form': form})
    
@login_required
def matches_view(request):
    user_profile = request.user.profile
    matches = find_matches(user_profile)
    return render(request, 'matches.html', {'matches': matches})
    
    
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile_detail')  # Redirecionar para a página de detalhes do perfil
    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {'form': form})
