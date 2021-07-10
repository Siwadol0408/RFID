from django.shortcuts import render

from django.http import HttpResponse


def index1(request):
    return HttpResponse("Counter1")
def index2(request):
    return HttpResponse("Counter2")    