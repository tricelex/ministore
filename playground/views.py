from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def calculate():
    x = 1
    y = 2
    return x + y


def sayHello(request):
    x = calculate()
    return render(request, "playground/hello.html", {"name": "Chiboy"})
