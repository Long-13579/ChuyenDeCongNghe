from django.core.management.base import BaseCommand
from datetime import date
from model_tutorial.models import Blog, Author, Entry


class Command(BaseCommand):
    help = "Initialize sample data for Blog, Author, and Entry models"

    def handle(self, *args, **kwargs):
        # Create some blogs
        blog1, _ = Blog.objects.get_or_create(
            name="Tech Talk",
            defaults={"tagline": "All about technology and coding."}
        )
        blog2, _ = Blog.objects.get_or_create(
            name="Travel Diaries",
            defaults={"tagline": "Adventures from around the world."}
        )

        # Create authors
        author1, _ = Author.objects.get_or_create(
            name="Alice Johnson", email="alice@example.com"
        )
        author2, _ = Author.objects.get_or_create(
            name="Bob Smith", email="bob@example.com"
        )

        # Create entries
        entry1, _ = Entry.objects.get_or_create(
            blog=blog1,
            headline="Introduction to Django",
            defaults={
                "body_text": "Django makes it easier to build better web apps more quickly.",
                "pub_date": date(2023, 6, 1),
                "number_of_comments": 2,
                "rating": 5,
            }
        )
        entry1.authors.set([author1, author2])

        entry2, _ = Entry.objects.get_or_create(
            blog=blog2,
            headline="Top 10 Travel Destinations",
            defaults={
                "body_text": "Here are the top 10 places you must visit once in your lifetime.",
                "pub_date": date(2023, 7, 15),
                "number_of_comments": 5,
                "rating": 4,
            }
        )
        entry2.authors.set([author2])

        self.stdout.write(self.style.SUCCESS("Sample data initialized successfully!"))
