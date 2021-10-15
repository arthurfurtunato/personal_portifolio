from django.db import models
#Migrate when you change de models, cause you telling that have a 
#new table on the db

class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portifolio/images/')
    description = models.CharField(max_length=250)
    url = models.URLField(blank=True)