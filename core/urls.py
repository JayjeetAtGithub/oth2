from django.conf.urls import url
from django.urls import path
from core import views

urlpatterns = [
	
	path('rules/',views.Rules.as_view()),
	path('leaderboard/',views.Leaderboard.as_view()),
	path('register/',views.RegisterUser.as_view()),

]