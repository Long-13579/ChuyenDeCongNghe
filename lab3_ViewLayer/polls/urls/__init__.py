from django.urls import include, path

urlpatterns = [
    path("view-function/", include("polls.urls.viewUrls")),
    path("view-class/", include("polls.urls.viewClassUrls")),
    path("template/", include("polls.urls.templateUrls"))
]
