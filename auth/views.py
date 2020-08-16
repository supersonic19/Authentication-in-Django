from django.http import HttpResponseRedirect
from django.shortcuts import render
from auth import forms
from django.contrib.auth import authenticate , login as auth_login

# Create your views here.

def login(request):
    loginForm = forms.LoginForm()
    error = None

    if request.method == "POST":
        loginForm = forms.LoginForm(request.POST)

        if loginForm.is_valid():
            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']

            user = authenticate(username = username,password = password)

            if user:
                auth_login(request , user)   # STARTS A SESSION FOR THIS USER
                return HttpResponseRedirect('/')
            else:
                error = "Invalid username and password"

    context = {
        'form' : loginForm,
        'error' : error
    }

    return render(request , 'auth/login.html' , context)
