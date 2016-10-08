from django.shortcuts import render
from django.http import response

# Create your views here.
def index(request):
    a=123
    return response('hello')