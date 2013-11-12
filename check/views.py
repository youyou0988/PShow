from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from student.models import Student
from algorithm.forms import addForm, updateForm
from algorithm.models import Algorithm
from globals.constants import ROOT
import os, shutil


def check_(request):
    student = None
    try:
        student = Student.objects.get(user = request.user)
    except:
        pass
    
    is_login = False
    if student:
        is_login = True
    else:
        return HttpResponseRedirect('/login/')
    
    algorithms = student.get_algorithm()
    addform = addForm()
    updateform = updateForm()
    
    return render_to_response('check.html', RequestContext(request, locals()))


def add_algorithm(request):
    student = None
    try:
        student = Student.objects.get(user = request.user)
    except:
        pass
    
    is_login = False
    if student:
        is_login = True
    else:
        return HttpResponseRedirect('/login/')
    
    error = list()
    sum = len(student.get_algorithm())
    if request.method == 'POST':
        form = addForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            if 'source' not in request.FILES:
                error.append('Add algorithm without source code')
            else :
                al = Algorithm.objects.create(name = name, owner = student, index=sum)
                al.save()
                
                # mkdir directory of nut
                source = request.FILES['source']
                nut = '%s/%s' % (ROOT, 'nut')
                dest = '%s/%s/%s/%s' % (ROOT, 'code', student.sid, name)
                if not os.path.exists(dest):
                    os.makedirs(dest, 0775)
                os.system('cp -r %s %s' % (nut, dest))
                
                # path
                path = '%s/%s' % (dest, 'nut/algorithm.cpp')
                file = open(path, 'wb+')
                for chunk in source.chunks():
                    file.write(chunk)
                file.close()
                
                os.system('rm -rf %s/nut/result' % dest)
                os.system('rm -rf %s/nut/evaluate' % dest)
                os.system('rm -rf %s/nut/main' % dest)
                os.system('rm -rf %s/nut/run' % dest)
                os.chdir('%s/nut' % dest)
                os.system('make')
                os.system('./main')
                os.system('./run')
                
                result = '%s/nut/result' % (dest)
                file = open(result, 'r+')
                re = file.readline()
                s = re.split(",")
                
                al.status = (int)(s[0])
                
                result = '%s/nut/evaluate' % (dest)
                file = open(result, 'r+')
                re = file.readline()
                s = re.split(",")
                al.time = (int)(s[0])
                al.space = (int)(s[1])
                al.save()
                # TODO
                # we should create the algorithm for student
    return HttpResponseRedirect('/check/')

def update_algorithm(request, index):
    student = None
    try:
        student = Student.objects.get(user = request.user)
    except:
        pass
    
    is_login = False
    if student:
        is_login = True
    else:
        return HttpResponseRedirect('/login/')
    
    al = Algorithm.objects.get(index = (int)(index))
    error = list()
    if request.method == 'POST':
        form = updateForm(request.POST, request.FILES)
        if form.is_valid():
            if 'source' not in request.FILES:
                error.append('Update algorithm without source code')
            else :
                source = request.FILES['source']
                dest = '%s/%s/%s/%s' % (ROOT, 'code', student.sid, al.name)
                
                # path
                path = '%s/%s' % (dest, 'nut/algorithm.cpp')
                file = open(path, 'wb+')
                for chunk in source.chunks():
                    file.write(chunk)
                file.close()
                
                os.system('rm -rf %s/nut/result' % dest)
                os.system('rm -rf %s/nut/evaluate' % dest)
                os.system('rm -rf %s/nut/main' % dest)
                os.system('rm -rf %s/nut/run' % dest)
                os.chdir('%s/nut' % dest)
                os.system('make')
                os.system('./main')
                os.system('./run')
                
                result = '%s/nut/result' % (dest)
                file = open(result, 'r+')
                re = file.readline()
                s = re.split(",")
                
                al.status = (int)(s[0])
                
                result = '%s/nut/evaluate' % (dest)
                file = open(result, 'r+')
                re = file.readline()
                s = re.split(",")
                al.time = (int)(s[0])
                al.space = (int)(s[1])
                al.save()
                # we should create the algorithm for student
    return HttpResponseRedirect('/check/')