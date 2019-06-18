from django.db import models

class Searched(models.Model):
	id_Film_Visited = models.CharField(max_length = 2)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return 'Película : '+self.id_Film_Visited+' Fecha de inserción: '+self.date.__str__()

