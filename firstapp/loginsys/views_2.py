# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login
from django.template.context_processors import csrf
# djbook django 1.9

def login(request):
    args = {}
    args.update(csrf(request))
#   print "test"
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('login.html', args)

    else:
        return render_to_response('login.html', args)


def logout(request):
    logout(request)
    return redirect("/")

