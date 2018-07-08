from rest_framework import serializers
from .models import Player , Level , TotalLevel
from django.contrib.auth.models import User


class PlayerSerializer(serializers.ModelSerializer):
	class Meta : 

		model = Player
		fields = '__all__'




class LevelSerializer(serializers.ModelSerializer):
	class Meta :

		model = Level
		fields = '__all__'



class TotalLevelSerializer(serializers.ModelSerializer):
	class Meta:

		model = TotalLevel
		fields = '__all__'



class LeaderboardSerializer(serializers.ModelSerializer):
	class Meta:

		model = Player
		fields = ('player_name','rank','score')


class UserSerializer(serializers.ModelSerializer):
	class Meta :

		model = User
		fields = '__all__'


		