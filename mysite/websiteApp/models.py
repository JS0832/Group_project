from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Access through User.profile.(field)
# Created with help from:
# simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_points = models.IntegerField(default=0)
    game_master = models.BooleanField(default=False)


# Taken from:
# simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Riddle(models.Model):
    question = models.TextField(max_length=250)
    answer = models.CharField(max_length=200)
    time = models.DateTimeField('date published')
    points = models.IntegerField()
    likes = models.IntegerField()


class Score(models.Model):
    username = models.CharField(max_length=30)
    time = models.DateTimeField('date published')
    points = models.IntegerField()
