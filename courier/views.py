from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "courier/index.html", context)

def about(request):
    context = {}
    return render(request, "courier/about.html", context)

def services(request):
    context = {}
    return render(request, "courier/services.html", context)

def contact(request):
    context = {}
    return render(request, "courier/contact.html", context)

def main(request):
    context = {}
    return render(request, "courier/main.html", context)