from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse


def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,
                            password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            context["error"] = "User Does Not Exist"
            return render(request, "users/login.html", context=context)
    else:
        if request.user.is_authenticated:
            return render(request, "lifecare/index.html")
        return render(request, "users/login.html", context=context)


@login_required()
def user_logout(request):
    logout(request)
    return render(request, "lifecare/index.html")

# Create your views here.
# def login(request):
#     if request.method == 'POST':
#         print("wow!!!!!!!!!!!!!!!!!!!!!")
#         messages.success(request, f'Welcome Back username!')
#         return render(request, 'lifecare/result.html')
#     else:
#         print("no!!!!!")
