from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(parameter_list):
    return HttpResponse("Hello Polls!")
