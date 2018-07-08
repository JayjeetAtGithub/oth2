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


	


'''

def index(request):

    m_level = models.total_level.objects.get(id=1)
    lastlevel = m_level.totallevel
    
    user = request.user
    print(user)
    if user.is_authenticated:
        player = models.player.objects.get(user_id=request.user.pk)
        try:
            level = models.level.objects.get(l_number=player.current_level)
            return render(request, 'level.html', {'player': player, 'level': level})
        except models.level.DoesNotExist:
            if player.current_level > lastlevel:
                return render(request, 'win.html', {'player': player})
            return render(request, 'finish.html', {'player': player})

    return render(request, 'index_page.html')

'''



class Index(APIView):

	def get(self,request,format=None):
		user = request.user
		print(user)
		return Response('idhwi')



		# if user.is_authenticated:
		# 	player = models.player.objects.get(user=user)
		# 	try:
		# 		level = Level.objects.get(level_number = player.current_level)
		# 		res = {}
		# 		res['player'] = player
		# 		res['level'] = level
		# 		return Response(res,status=200)
		# 	except Level.DoesNotExist:
		# 		if player.current_level > last_level:
		# 			res = {}
		# 			res['player'] = player
		# 			res['level'] = 'win'
		# 			return Response(res,status=200)
		# 		else:
		# 			res = {}
		# 			res['player'] = player
		# 			res['level'] = 'finish'
		# 			return Response(res,status=200)

		# return Response('index_page')
			











##"EAAG8BjuZC4O8BABF9ZBDw0iCsYspf34reT2iTOa7ADcUBwcrGCoaV1iY1FCZApLHMTR4gABz2ZALeifwqPQ4fusD1lH4ZA77QKG5Mr9ZAzZCjZCnfxS2xI8mJiTs93sssOqczXVfGv718VK3yKIipvQkwSk8D2eiBZARmy3Hjj4LAiGg1ApnnR8BJoKSezytiLUkZALsobPKpKBQZDZD"
##"EAAG8BjuZC4O8BALI31JjvDnVFPs51ZAmnxR7EcNbINju7xaO3pmZBXSzh2rPvg5eiBnmfHlUNFT8wZCKzSliOjZA1eV0OwmLmf4t5PuB14JffDFZAxUcNj4F2YQbux9LRwyu9JZBD1lZA5nhppbPbAD4M0sYPsfvXyw7R4PYQZAswwbLfP8a3NQG9G0f0UG5aCZClrWS4VFQ3AhgZDZD"