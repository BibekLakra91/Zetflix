from django.http import HttpResponse
from django.shortcuts import render


def zetflix(request):
    return render(request, 'index.html')
def add(request):
    return HttpResponse("Hello world! add page")
def remove(request):
    return HttpResponse("Hello world! remove page")
def list(request):
    return HttpResponse("Hello world! list page")
