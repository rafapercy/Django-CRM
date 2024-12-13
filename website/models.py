from django.db import models


class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	album_title = models.CharField(max_length=500)
	artist_name = models.CharField(max_length=500)
	release_year = models.CharField(max_length=500)
	genre = models.CharField(max_length=500)
	inclusions = models.CharField(max_length=1000)

	def __str__(self): 
		return(f"{self.album_title} {self.artist_name}")