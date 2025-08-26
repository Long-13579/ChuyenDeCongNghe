from django.urls import path
from polls.views.viewClassBase import AboutView, BookListView, AsyncView

urlpatterns = [
    path("about/", AboutView.as_view(), name="about"),
    path("books/", BookListView.as_view(), name="book-list"),
    path("async/", AsyncView.as_view(), name="async-view"),
]
