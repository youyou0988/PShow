# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from student.models import Student
from algorithm.models import Algorithm

def info(request):
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
    
    student_rank = Student.objects.all().order_by('-score')[0:10]
    algorithm_space = Algorithm.objects.filter(status = 0).order_by('space')[0:10]
    algorithm_time = Algorithm.objects.filter(status = 0).order_by('time')[0:10]
    
    return render_to_response('info.html', RequestContext(request, locals()))

