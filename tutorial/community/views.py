from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def write(request):
    return render(request, 'index.html')

def list(request):
    return HttpResponse("Hello world, your in index world")
    
