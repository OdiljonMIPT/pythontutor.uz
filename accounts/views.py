from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import UserAdminCreationForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')

    return render(request, 'pages/login.html', {})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login')

    return render(request, 'pages/logout.html', {})


def register_view(request):
    form = UserAdminCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/login')
    context = {
        'form': form
    }
    return render(request, 'pages/register.html', context)


@login_required
def profile_view(request):
    return render(request, 'pages/profile.html')
