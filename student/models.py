from django.db import models
from django.contrib.auth.models import User
from show.models import Show
from globals.constants import NAMELENGTH, IDLENGTH

class Student(models.Model):
    # for user management
    user = models.OneToOneField(User, unique = True)
    
    # student name 
    name = models.CharField(max_length = NAMELENGTH)
    
    # student id 
    sid = models.CharField(max_length = IDLENGTH)

    # student score
    score = models.IntegerField(default = 0)

    # show algorithm
    show = models.OneToOneField(Show, unique = True)
    
    # return all the algorithm which student submit
    def get_algorithm(self):
        return self.own_algorithm.all()
    