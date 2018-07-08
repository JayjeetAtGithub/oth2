from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Player , Level , TotalLevel
from .serializers import PlayerSerializer , LevelSerializer , TotalLevelSerializer , LeaderboardSerializer , UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from datetime import datetime


class Leaderboard(APIView):

	def get(self,request,format=None):
		player_rank_list = Player.objects.order_by('-score','timestamp')
		rank_counter = 1

		for player in player_rank_list :
			player.rank = rank_counter
			player.save()
			rank_counter += 1

		players = Player.objects.all()
		serializer = LeaderboardSerializer(players,many=True)
		return Response(serializer.data)




class Rules(APIView):

	def get(self,request,format=None):
		return Response('Rules')


'''

username : userId obtained from google or facebook

'''

class RegisterUser(APIView):

	def post(self,request,format=None):
		current_user = User.objects.filter(username=request.data['username']).first()
		if current_user is not None:
			serializer = UserSerializer(current_user)
			return Response(serializer.data)
		else:
			user = User.objects.create_user(request.data['username'])
			user.email = request.data['email']
			user.first_name = request.data['first_name']
			user.last_name = request.data['last_name']
			user.save()
			player = Player(user=user , player_name = user.first_name + " " + user.last_name)
			player.save()
			serializer = UserSerializer(user)
			return Response(serializer.data,status=status.HTTP_201_CREATED)


	














