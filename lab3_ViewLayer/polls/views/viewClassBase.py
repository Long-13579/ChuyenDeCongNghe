import asyncio
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView
from polls.models import Book  # Adjust import to match your project

# Generic TemplateView subclass
class AboutView(TemplateView):
    template_name = "about.html"

# ListView with custom HEAD support
class BookListView(ListView):
    model = Book

    def head(self, *args, **kwargs):
        last_book = self.get_queryset().latest("publication_date")
        response = HttpResponse(
            headers={
                "Last-Modified": last_book.publication_date.strftime(
                    "%a, %d %b %Y %H:%M:%S GMT"
                )
            }
        )
        return response

# Asynchronous view example
class AsyncView(View):
    async def get(self, request, *args, **kwargs):
        await asyncio.sleep(1)
        return HttpResponse("Hello async world!")
