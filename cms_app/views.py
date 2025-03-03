from django.shortcuts import render
from django.contrib.auth import (
    authenticate,
    login as auth_login,
    logout as auth_logout
)
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.
def index(request):
    context = None
    if request.user.is_authenticated:
        context = {
            'username': request.user.username,
            'is_staff': request.user.is_staff,
            'email': request.user.email
        }
    return render(request, 'index.html', context)

def about(request):
    context = {
        "title": "About",
        "isShow": True
    }
    return render(request, 'about.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            auth_login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials or not an admin user'})
    
    return render(request, 'login.html')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('index')