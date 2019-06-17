from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.template.loader import render_to_string
from django.http import Http404, HttpResponseRedirect, HttpResponse, StreamingHttpResponse
from wars.forms import searchForm
import requests


class main(TemplateView):
	def get(self,request):
		form=searchForm()
		return render(request, 'index.html', {'form': form,})

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
		film = nameFilm
		context = {'film':film, 'lista_films':lista_films}
		return (context)
	template_name = "film.html"


class character(TemplateView):
	template_name = "Timer.html"

