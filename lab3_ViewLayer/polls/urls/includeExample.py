from django.urls import include, path

urlpatterns = [
    # ... other patterns ...
    path("community/", include("aggregator.urls")),
    path("contact/", include("contact.urls")),
    # ... other patterns ...
]
