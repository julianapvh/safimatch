from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True)
    interests = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class Swipe(models.Model):
    swiper = models.ForeignKey(User, related_name='swipes', on_delete=models.CASCADE)
    swiped = models.ForeignKey(User, related_name='swiped', on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
