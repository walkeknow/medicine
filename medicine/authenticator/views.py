from django.shortcuts import render, get_object_or_404, HttpResponse
from django.template.defaulttags import register

# Create your views here.
def index(request):
    return render(request, 'lifecare/index.html')


def login(request):
    return render(request, 'lifecare/login.html')


def results(request):
    return render(request, 'lifecare/result.html')


def upload(request):
    return HttpResponse("<h2>Lmao, you actually thought "
                        "this page was made?</h2>")
