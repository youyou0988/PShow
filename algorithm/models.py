from django.db import models
from student.models import Student
from globals.constants import NAMELENGTH, DIRLENGTH

class Algorithm(models.Model):
    # Algorithm index of one student
    index = models.IntegerField(default = 0)
    
    # Algorithm name
    name = models.CharField(max_length = NAMELENGTH)
    
    # Algorithm source directory
    dir = models.CharField(max_length = DIRLENGTH)
    
    # Which student submit this algorithm
    owner = models.ForeignKey(Student, related_name = 'own_algorithm')
    
    # Time for run this algorithm
    time = models.IntegerField(default = 0)
    
    # Space for run this algorithm
    space = models.IntegerField(default = 0)
