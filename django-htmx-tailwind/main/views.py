from django.shortcuts import render
from django.http import HttpResponse

# simple in-memory counter (server-side)
COUNTER = 0

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def counter(request):
    global COUNTER
    COUNTER += 1
    return HttpResponse(f'<div id="counter"><button hx-get="/counter/" hx-swap="outerHTML" class="px-4 py-2 bg-blue-600 text-white rounded">Incremented: {COUNTER}</button></div>')