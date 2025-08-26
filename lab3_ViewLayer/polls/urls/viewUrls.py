from django.urls import path
from polls import viewFunction

urlpatterns = [
    path("time/", viewFunction.current_datetime, name="current-datetime"),
    path("myview/", viewFunction.my_view, name="my-view"),
    path("polls/<int:poll_id>/", viewFunction.detail, name="poll-detail"),
    path("edit/<int:pk>/", viewFunction.edit, name="edit-view"),
    path("error/", viewFunction.response_error_handler, name="error-handler"),
]
