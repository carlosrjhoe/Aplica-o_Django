from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Bolos da May</h1><h2>Bem vindos aos melhores bolos da região</h2>')