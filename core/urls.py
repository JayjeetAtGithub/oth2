from django.conf.urls import url
from django.urls import path , include
from core import views

urlpatterns = [
	
	path('rules/',views.Rules.as_view()),
	path('leaderboard/',views.Leaderboard.as_view()),
	path('register/',views.RegisterUser.as_view()),
	path('answer/',views.Answer.as_view()),
	path('',views.Index.as_view()),
	path('auth/', include('rest_framework_social_oauth2.urls')),

]


