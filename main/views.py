from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from main.forms import RegisterForm, LoginForm
from django.http import HttpResponseRedirect
from student.models import Student
from show.models import Show

import re
SHA1_RE = re.compile('^[a-f0-9]{40}$')

def register_(request):
    student = None
    try:
        student = Student.objects.get(user = request.user)
    except:
        pass
    
    if student:
        HttpResponseRedirect('/')
    
    error = list()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            sid = form.cleaned_data['sid']
            name = form.cleaned_data['name']
            pwd = form.cleaned_data['pwd']
            pwdc = form.cleaned_data['pwdc']
            
            if pwd != pwdc:
                error.append('Password Different')
                
            tmp = None
            try:
                tmp = Student.objects.get(sid = sid)
            except:
                pass
            if tmp:
                error.append('Student has been registered')

            if len(error) == 0:
                    user = User.objects.create(username = sid, password = pwd, is_active = True)
                    user.set_password(pwd)
                    user.save()
                    show = Show.objects.create()
                    show.save()
                    student = Student.objects.create(user = user, name = name, sid = sid, show = show)
                    
                    user = authenticate(username = user.username, password = pwd)
                    login(request, user)
                    return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
    return render_to_response('register.html', RequestContext(request, locals()))

def login_(request):
    student = None
    try:
        student = Student.objects.get(user = request.user)
    except:
        pass
    
    if student:
        return HttpResponseRedirect('/')
    
    error = list()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            sid = form.cleaned_data['sid']
            pwd = form.cleaned_data['pwd']
            
            try:
                user = authenticate(username = sid, password = pwd)
                if not user:
                    error.append('Student can not match Password')
                else:
                    login(request, user)
                    student = Student.objects.get(user = user)
                    if len(error) == 0:
                        return HttpResponseRedirect('/')
            except:
                error.append('Login Failed')
    else:
        form = LoginForm()
    return render_to_response('login.html', RequestContext(request, locals()))

def logout_(request):
    logout(request)
    return HttpResponseRedirect('/')

def main(request):
    student = None
    try:
        student = Student.objects.get(user = request.user)
    except:
        pass
    
    is_login = False
    if student:
        is_login = True
        
    return render_to_response('index.html', RequestContext(request, locals()))