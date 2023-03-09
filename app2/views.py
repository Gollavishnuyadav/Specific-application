from django.shortcuts import render

from django.http import HttpResponse

def two(request):
    return HttpResponse("two")
