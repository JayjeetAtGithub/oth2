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

		user = request.user
		if user.is_authenticated:
			player_rank_list = Player.objects.order_by('-score','timestamp')
			rank_counter = 1

			for player in player_rank_list :
				player.rank = rank_counter
				player.save()
				rank_counter += 1

			players = Player.objects.all()
			serializer = LeaderboardSerializer(players,many=True)
			return Response(serializer.data)
		return Response("Unauthenticated")




class Rules(APIView):

	def get(self,request,format=None):
		user = request.user
		if user.is_authenticated:
			return Response('Rules')
		return Response("Unauthenticated")




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


	

class Index(APIView):

	def get(self,request,format=None):

		last_level = TotalLevel.objects.filter(id=1).first().total_level
		user = request.user
		if user.is_authenticated:
			player = Player.objects.filter(user=user).first()
			try:
				level = Level.objects.filter(level_number=player.current_level)
				return Response("level")
			except Level.DoesNotExist:
				if player.current_level > last_level:
					return Response("win")
				return Response("finish")
		return Response("index")



class Answer(APIView):

	def post(self,request,format=None):

		last_level = TotalLevel.objects.filter(id=1).first()
		ans = request.data['ans']
		user = request.user
		if user.is_authenticated:
			player = Player.objects.filter(user=user).first()
			try:
				level = Level.objects.filter(level_number=player.current_level)
			except Level.DoesNotExist:
				if player.current_level > last_level:
					return Response("win")
				return Response("finish")

			if ans == level.answer:
				player.current_level = player.current_level + 1
				player.score = player.score + 10
				player.timestamp = datetime.now
				level.number_of_user = level.number_of_user + 1
				level.accuracy = round(level.number_of_user/(float(level.number_of_user + level.wrong)),2)
				level.save()
				player.save()
				try:
					level = Level.objects.filter(level_number=player.current_level).first()
					return render(request, 'level_transition.html')
					return Response("level")
				except:
					if player.current_level > last_level:
						return Response("win") 
					return Response("finish")

			elif ans == "":
				pass

			else:
				level.wrong = level.wrong + 1
				level.save()
		return Response("Unauthorized")





