from django.template.loader import get_template, render_to_string
from django.http import HttpResponse

def manual_view(request):
    template = get_template('polls/item_list.html')
    content = template.render({'items': [{'name': 'pen', 'price': 100}, {'name': 'notebook', 'price': 200}]}, request)
    return HttpResponse(content)

from django.shortcuts import render

def quick_view(request):
    return render(request, 'polls/item_list.html', {'items': [{'name': 'pen', 'price': 100}, {'name': 'notebook', 'price': 200}]})
