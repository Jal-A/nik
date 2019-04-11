from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("i am in second app")
# Create your views here.
