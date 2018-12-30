from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['USERNAME'],password=request.POST['PASSWORD'])
        if user is not None:
            auth.login(request,user)
            return redirect('product_home')
        else:
            return render(request, 'login.html', {'error': 'user name or passwor is incorrect'})
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['PASSWORD1'] == request.POST['PASSWORD2']:
            try:
                user = User.objects.get(username = request.POST['USERNAME'])
                return render(request, 'signup.html', {'error': 'the username has been already taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['USERNAME'], password=request.POST['PASSWORD1'])
                auth.login(request, user)
                return redirect('product_home')
        else:
            return render(request, 'signup.html', {'error': 'the password does not match!'})
    else:
        return render(request, 'signup.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('product_home')
