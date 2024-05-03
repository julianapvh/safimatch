from .models import Profile

def find_matches(user_profile):
    # Exemplo básico: encontrar perfis com idade semelhante
    user_age = user_profile.age
    matching_profiles = Profile.objects.exclude(user=user_profile.user).filter(age=user_age)
    return matching_profiles
