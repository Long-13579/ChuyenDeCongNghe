from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.http import Http404
import datetime

# 1. Simple current_datetime view
def current_datetime(request):
    now = datetime.datetime.now()
    html = f'<html lang="en"><body>It is now {now}.</body></html>'
    return HttpResponse(html)

# 2. View returning 404 or regular response
def my_view(request):
    foo = False  # Replace with actual condition
    if foo:
        return HttpResponseNotFound("<h1>Page not found</h1>")
    else:
        return HttpResponse("<h1>Page was found</h1>")

# 3. View that raises Http404
from polls.models import Poll  
def detail(request, poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, "polls/detail.html", {"poll": p})

# 4. View that raises PermissionDenied
def edit(request, pk):
    # Example: only staff users may edit
    if not request.user.is_staff:
        raise PermissionDenied
    # Continue editing logic here...
    return HttpResponse("You can edit.")

# 5. Custom error handler for testing (e.g., 403)
def response_error_handler(request, exception=None):
    return HttpResponse("Error handler content", status=403)
