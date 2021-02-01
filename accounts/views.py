from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *


def user_register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            form = RegistrationForm(request.POST or None)
            if form.is_valid():
                user = form.save()

                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=user.username,
                                    password=raw_password)

                login(request, user)
                return redirect('index')
        else:
            form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return render(request, 'login.html', {'error': 'Your account has been disabled.'})
            else:
                return render(request, 'login.html', {'error': 'Invalid Username or Password. Try Again.'})
    return render(request, 'login.html')


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
