from django.urls import path
from polls.views import viewTemplate

urlpatterns = [
    path("manual/", viewTemplate.manual_view, name="manual"),
    path("quick/", viewTemplate.quick_view, name="quick"),
]
