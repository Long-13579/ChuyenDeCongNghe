from django.db import models

# Create your models here.
class Poll(models.Model):
    detail = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    class Meta:
        ordering = ["-publication_date"]  # newest books first

    def __str__(self):
        return f"{self.title} by {self.author}"
