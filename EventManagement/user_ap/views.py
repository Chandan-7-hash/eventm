from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return render(request, f'Account created for {username}!')
        return HttpResponseRedirect('login')  
    else:
        form = UserRegisterForm()
        d = {'form': form}
    return render(request, 'register.html', d)

def user_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        AUO = authenticate(username=un, password=pw)
        if AUO:
            login(request, AUO)
            request.session['username'] = un
            d = {'user': AUO}
            return render(request, 'user_login.html', d)
        return HttpResponse('invalid Creds')
    return render(request, 'user_login.html')


def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return HttpResponseRedirect(render('home'))