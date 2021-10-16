from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    date_post = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=200)
