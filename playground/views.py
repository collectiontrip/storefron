from django.shortcuts import render
from django.http import HttpResponse


def say_hy(request):
    return HttpResponse("Hello World")
