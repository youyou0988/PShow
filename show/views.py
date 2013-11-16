from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from student.models import Student
from show.forms import showForm, piForm
from show.models import next_p_, pre_p_, index_p_, permutation_p_

def show_(request):
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
    
    error= list()
    if request.method == 'POST':
        form = showForm(request.POST, request.FILES)
        if form.is_valid():
            length = form.cleaned_data['length']
            type = form.cleaned_data['type']
            
            student.show.length = (int)(length)
            student.show.type = (int)(type)
            
            student.show.save()
    else:
        form = showForm(instance = student.show)
    
    current_p = 0
    num = 1
    current_idx=0
    current_i=0
    #current_idx,current_i = index_p_(student.show, current_p)	
    piform = piForm(initial={'permutation':current_p, 'middle':current_idx,'index':current_i,'num':num,'oldpermutation':current_p,'oldmiddle':current_idx,'oldindex':current_i})
    
    return render_to_response('show.html', RequestContext(request, locals()))

def action(request):
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
    
    form = showForm(instance = student.show)
    # for next_p
    if request.method == 'POST' and 'next_p' in request.POST:
        piform = piForm(request.POST)
        if piform.is_valid():
            current = piform.cleaned_data['oldpermutation']
            num = piform.cleaned_data['num']
            
            #current_op = next_p_(student.show, current)
            old_idx,old_index = index_p_(student.show, current)
            new_index = old_index + int(num)
            new_idx,new_p = permutation_p_(student.show,new_index)
            
            piform = piForm(initial={'num':num,'permutation':new_p,'middle':new_idx,'index':new_index,'oldpermutation':current,'oldmiddle':old_idx,'oldindex':old_index})
    # form pre_p
    elif request.method == 'POST' and 'pre_p' in request.POST:
        piform = piForm(request.POST)
        if piform.is_valid():
            current = piform.cleaned_data['oldpermutation']
            num = piform.cleaned_data['num']
            old_idx,old_index = index_p_(student.show, current)
            new_index = old_index - int(num)
            new_idx,new_p = permutation_p_(student.show,new_index)
            piform = piForm(initial={'num':num,'permutation':new_p,'middle':new_idx,'index':new_index,'oldpermutation':current,'oldmiddle':old_idx,'oldindex':old_index})
    # for index_p
    elif request.method == 'POST' and 'index_p' in request.POST:
        piform = piForm(request.POST)
        if piform.is_valid():
            current = piform.cleaned_data['permutation']
            
            current_p = current
            current_idx,current_i = index_p_(student.show, current)
            
            piform = piForm(initial={'permutation':current_p, 'middle':current_idx,'index':current_i,'num':1,'oldpermutation':current_p,'oldmiddle':current_idx,'oldindex':current_i})
    # for permutation_p
    elif request.method == 'POST' and 'permutation_p' in request.POST:
        piform = piForm(request.POST)
        if piform.is_valid():
            index = piform.cleaned_data['index']
            
            current_idx,current_p = permutation_p_(student.show, index)
            current_i = index
            piform = piForm(initial={'permutation':current_p, 'middle':current_idx,'index':current_i,'num':1,'oldpermutation':current_p,'oldmiddle':current_idx,'oldindex':current_i})
    
    return render_to_response('show.html', RequestContext(request, locals()))
