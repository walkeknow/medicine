from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def login(request):
    if request.method == 'POST':
        messages.success(request, f'Welcome Back username!')
        return redirect('index')
