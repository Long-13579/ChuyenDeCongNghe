import os
import django
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
django.setup()

from model_tutorial.models import *

# Get all
all_entries = Entry.objects.all()
print(all_entries)

# Filter
filted_entry = Entry.objects.filter(pub_date__year=2023)
print(filted_entry)

# Chain filter
filted_entry = Entry.objects.filter(headline__startswith="What").exclude(
    pub_date__gte=date.today()
).filter(pub_date__gte=date(2005, 1, 30))
print(filted_entry)

# Lazy filter
q = Entry.objects.filter(headline__startswith="Introduction")
q = q.filter(pub_date__lte=date.today())
q = q.exclude(body_text__icontains="food")
print(q)

# Get specifit record
filted_entry = one_entry = Entry.objects.get(pk=1)
print(filted_entry)

# Limiting Query
Entry.objects.all()[:5]
Entry.objects.all()[5:10]
Entry.objects.all()[:10:2]
Entry.objects.order_by("headline")[0]
Entry.objects.order_by("headline")[0:1].get()