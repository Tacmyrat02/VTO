from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':  # Şert başlangyjy
        form = AuthenticationForm(request, data=request.POST)  # Indent edilen blok
        if form.is_valid():  # Içki şert
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:  # Içki şert
                login(request, user)
                return redirect('profile')  # Indent edilen blok
    else:  # Else şerti
        form = AuthenticationForm()  # Indent edilen blok
    return render(request, 'accounts/login.html', {'form': form})  # Funksiýanyň dowamy

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import UserChangeForm

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('tryon:home')
    else:
        form = UserChangeForm(instance=request.user)
    
    return render(request, 'accounts/profile.html', {
        'form': form,
        'body_data': request.user.get_body_data()
    })