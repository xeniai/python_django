#from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bonjour, world! Tu as le polls index.")
