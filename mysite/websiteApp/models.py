from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    total_points = models.IntegerField()
    game_master = models.BooleanField()
    
class Riddles(models.Model):
    question = models.TextField(max_length=250)
    answer = models.CharField(max_length=200)
    time = models.DateTimeField('date published')
    points = models.IntegerField()
    likes = models.IntegerField()
    
class Score(models.Model):
    username = models.CharField(max_length=30)
    time = models.DateTimeField('date published')
    points = models.IntegerField()
