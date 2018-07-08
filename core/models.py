from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Player(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    player_name = models.CharField(max_length=128)
    current_level = models.IntegerField(default=1)
    score = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.player_name



class Level(models.Model):

    level_number = models.IntegerField()
    question_image = models.ImageField(upload_to = 'images',default='images/level1.jpg') #ISSUE  :  THE DEFAULT FILE ARE
    question_audio = models.FileField(upload_to = 'audios',default='audios/default.mp3') #          NOT PRESENT
    question_body = models.TextField()
    question_answer = models.CharField(max_length=200)
    number_of_user = models.IntegerField(default=0)
    accuracy = models.FloatField(default=0)
    wrong = models.IntegerField(default=0)

    def __str__(self):
        return self.question_body




class TotalLevel(models.Model):
    
    total_level = models.IntegerField(default=100)

    def __str__(self):
        return str(self.total_level)
