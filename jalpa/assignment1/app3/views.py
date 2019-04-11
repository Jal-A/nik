

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("i am in third app")
# Create your views here.
