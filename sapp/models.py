from pyexpat import model
from django.db import models

# Create your models here.
class HomeContent(models.Model):
    contentId = models.IntegerField(default=1234)
    title = models.CharField(max_length=500)
    content = models.TextField()
