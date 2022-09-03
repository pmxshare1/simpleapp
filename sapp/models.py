from django.db import models

# Create your models here.
class HomeContent(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
