from django.contrib import admin
from django.urls import path
from wars import views

urlpatterns = [
	
	path('index/',views.main.as_view()),
	path('Character/',views.character.as_view()),
	path('Films/', views.films.as_view()),
	path('Film/<str:nameFilm>', views.film.as_view()),
]