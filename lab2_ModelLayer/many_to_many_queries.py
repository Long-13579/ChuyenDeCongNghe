import os
import django
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
django.setup()

from model_tutorial.models import *

# Create 
b = Blog(name="Beatles Blog", tagline="All the latest Beatles news.")
b.save()

# Saving Foreign key
entry = Entry.objects.get(pk=1)
cheese_blog = Blog.objects.get(name="Tech Talk")
entry.blog = cheese_blog
entry.save()
print(entry.blog)

joe = Author.objects.create(name="Joe")
entry.authors.add(joe)
print(entry.authors.all())

john = Author.objects.create(name="John")
paul = Author.objects.create(name="Paul")
george = Author.objects.create(name="George")
ringo = Author.objects.create(name="Ringo")
entry.authors.add(john, paul, george, ringo)
print(entry.authors.all())