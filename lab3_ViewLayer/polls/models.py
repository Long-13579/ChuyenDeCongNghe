from django.db import models

# Create your models here.
class Poll(models.Model):
    detail = models.CharField(max_length=50)