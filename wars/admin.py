from django.contrib import admin
from django import forms
from django.db import models
from wars.models import Searched

class ejemplarStacked(admin.StackedInline):
	model = Searched

admin.site.register(Searched)