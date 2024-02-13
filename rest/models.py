from django.db import models

# Create your models here.
class BlogPost(models.Model):
	title = models.CharField(max_length=200)
	content = models.CharField(max_length = 500)
	owner = models.CharField(max_length = 50)
	Headquarters = models.CharField(max_length = 50)
	Founded = models.IntegerField(null = True, blank = True)
	def __str__(self):
		return self.title