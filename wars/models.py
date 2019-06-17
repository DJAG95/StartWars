from django.db import models

class Searched(models.Model):
	id_Film = models.CharField(max_length = 2)
	date = models.DateField()

	def __str__(self):
		return 'Api utilizada: '+self.ApiURL+' Fecha de inserción: '+self.date

