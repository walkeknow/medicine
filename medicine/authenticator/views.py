from django.shortcuts import render, get_object_or_404, HttpResponse
from django.template.defaulttags import register
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'lifecare/index.html')


def results(request):
    return render(request, 'lifecare/result.html')


@login_required()
def upload_form(request):
    return render(request, 'lifecare/upload-form.html')


@login_required()
def upload_excel(request):
    return render(request, 'lifecare/upload-excel.html')
