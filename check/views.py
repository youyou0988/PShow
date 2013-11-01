from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from student.models import Student
from algorithm.forms import addForm, updateForm
from algorithm.models import Algorithm

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
    if request.method == 'POST':
        form = addForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            if 'source' not in request.FILES:
                error.append('Add algorithm without source code')
            else :
                source = request.FILES['source']
                al = Algorithm.objects.create(name = name, owner = student)
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
    
    error = list()
    if request.method == 'POST':
        form = updateForm(request.POST, request.FILES)
        if form.is_valid():
            if 'source' not in request.FILES:
                error.append('Update algorithm without source code')
            else :
                source = request.FILES['source']
                # TODO
                # we should create the algorithm for student
    return HttpResponseRedirect('/check/')