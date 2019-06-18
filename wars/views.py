from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.template.loader import render_to_string
from wars.models import Searched
from django.http import Http404, HttpResponseRedirect, HttpResponse, StreamingHttpResponse
from wars.forms import searchForm
import requests


class main(TemplateView):
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		form=searchForm()
		searched = Searched.objects.order_by('date').reverse()[:12]
		context = {'form': form, 'searched':searched, }
		return (context)
	template_name = "index.html"

	def post(self, request):
		final = request.POST.get('search')
		return HttpResponseRedirect("../Film/"+final)


class films(TemplateView):

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		lista_films = requests.get('https://swapi.co/api/films/').json()
		context = {'lista_films':lista_films}
		return (context)
	template_name = "films.html"

class film(TemplateView):

	def get_context_data(self, nameFilm):
		context = super().get_context_data()
		lista_films = requests.get('https://swapi.co/api/films/').json()
		film = None
		for i in lista_films['results']:
			if i['title'].upper() == nameFilm.upper():
				film = i
				newEntry = Searched(id_Film_Visited=i['episode_id'],)
				newEntry.save()
		context = {'film':film}
		return (context)
	template_name = "film.html"
	


class character(TemplateView):
	template_name = "Timer.html"

