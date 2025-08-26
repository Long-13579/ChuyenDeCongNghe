from django.urls import include, path

urlpatterns = [
    path("view-function/", include("polls.urls.viewUrls")),
]
