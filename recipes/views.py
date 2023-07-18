from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "recipes/home.html", status=201)


def _contato(request):
    return render(request, "me-apague.temp.html")


def _base(request):
    return HttpResponse("Base")
