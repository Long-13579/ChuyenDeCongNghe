import os
import django
from datetime import date
from django.db.models import F, OuterRef, Subquery, Sum

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
django.setup()

from model_tutorial.models import *

filted_entry = Entry.objects.filter(pub_date__lte="2026-01-01")
print(filted_entry)

filted_entry = Entry.objects.filter(blog_id=4)
print(filted_entry)

filted_entry = Entry.objects.get(headline__exact="Introduction to Django")
print(filted_entry)

filted_entry = Entry.objects.get(headline__contains="Travel")
print(filted_entry)

filted_entry = Entry.objects.filter(blog__name="Tech Talk")
print(filted_entry)

filted_entry = Blog.objects.filter(entry__headline__contains="Travel")
print(filted_entry)

filted_entry = Blog.objects.filter(entry__authors__name="Bob Smith")
print(filted_entry)

filted_entry = Blog.objects.filter(entry__headline__contains="Travel", entry__pub_date__year=2023)
print(filted_entry)

filted_entry = Entry.objects.filter(number_of_comments__gt=F("number_of_pingbacks"))
print(filted_entry)

queries_result = Entry.objects.values("pub_date__year").annotate(
    top_rating=Subquery(
        Entry.objects.filter(
            pub_date__year=OuterRef("pub_date__year"),
        )
        .order_by("-rating")
        .values("rating")[:1]
    ),
    total_comments=Sum("number_of_comments"),
)
print(queries_result)