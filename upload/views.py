from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def upload(request):
    return HttpResponse('<h1>Upload Screen</h1>')
