from django.db import models
from globals.constants import DICTIONARY, INCREASE, DECREASE, SWITCH, DEPLENGTH
from algorithm.methods import Dictionary, Increase, Decrease, Switch

# Next Permutation
nextp = {
               DICTIONARY : Dictionary.next,
               INCREASE : Increase.next,
               DECREASE : Decrease.next,
               SWITCH : Switch.next,
               }

# Previous Permutation
prep = {
               DICTIONARY : Dictionary.previous,
               INCREASE : Increase.previous,
               DECREASE : Decrease.previous,
               SWITCH : Switch.previous,
               }

# Permutation to Index
p2index = {
               DICTIONARY : Dictionary.index,
               INCREASE : Increase.index,
               DECREASE : Decrease.index,
               SWITCH : Switch.index,
               }

# Index to Permutation
index2p = {
               DICTIONARY : Dictionary.permutation,
               INCREASE : Increase.permutation,
               DECREASE : Decrease.permutation,
               SWITCH : Switch.permutation,
               }

class Show(models.Model):
    # length for permutation
    length = models.IntegerField(default = DEPLENGTH)
    
    # type for permutation
    type = models.IntegerField(default = DICTIONARY)
    

# return [current]'s next permutation, while length & type defined in [show]
def next_p_(show, current):
    return nextp[show.type](show.length, current)

# return [current]'s previous permutation, while length & type defined in [show]
def pre_p_(show, current):
    return prep[show.type](show.length, current)

# return [current] permutation's index, while length & type defined in [show]
def index_p_(show, current):
    return p2index[show.type](show.length, current)

# return the [index]'s permutation, while length & type defined in [show]
def permutation_p_(show, index):
    return index2p[show.type](show.length, index)
