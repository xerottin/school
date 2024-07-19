from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from users import forms
from users.forms import SignUpForm


def sign_up(request):
    form = SignUpForm(request.POST or None)
    is_success = False
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('users:sign_in')
    return render(request, 'sign_up.html', {
        'form': form,
        'is_success': is_success,
    })


def sign_in(request):
    form = forms.SignInForm(data=request.POST or None)
    is_success = False
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('course:index')
    return render(request, 'sign_in.html', {
        'form': form,
        'is_success': is_success,
    })


def sign_out(request):
    logout(request)
    return redirect('users:sign_in')
