from django.contrib.auth import authenticate as dj_auth, login as dj_login, logout as dj_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_GET


@require_GET
def login_view(request: HttpRequest):
    return render(request, 'users/login.html')


@require_POST
def login_done(request: HttpRequest):
    if not request.user.is_anonymous:
        return redirect('main_application:index_url')
    if 'username' in request.POST and len(request.POST['username']) != 0:
        username = request.POST['username']
    else:
        return redirect('users:login_url')
    if 'password' in request.POST and len(request.POST['password']) != 0:
        password = request.POST['password']
    else:
        return redirect('users:login_url')

    user = dj_auth(username=username, password=password)
    if user is not None:
        dj_login(request, user)
        return redirect('main_application:index_url')
    return redirect('users:login_url')


@require_POST
@login_required
def logout_done(request: HttpRequest):
    dj_logout(request)
    return redirect('users:login_url')
