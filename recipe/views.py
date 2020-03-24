from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    return HttpResponse("done")

def search(request):
    return render(request, 'recipe/index.html', {
        'foo' : 'bar'
    })