from globals.constants import OVERFLOW, ERROR, WARNING

# Dictionary Permutation Method
# [n] indicate the permutation length
# for test permutation type, next = add 1, previous = subtract 1, p2index = add 10, index2p = subtract 10
# for test permutation length, more n variables base last step test 
class Dictionary:
    
    # return the [current] permutation's next permutation 
    @staticmethod
    def next(n, current):
        #TODO
        return (int)(current) + 1 + n
    
    # return the [current] permutation's previous permutation 
    @staticmethod
    def previous(n, current):
        #TODO
        return (int)(current) - 1 - n
    
    # return the [current] permutation's index
    @staticmethod
    def index(n, current):
        #TODO
        return (int)(current) + 10 + n
    
    # return the [index] permutation
    @staticmethod
    def permutation(n, index):
        #TODO
        return (int)(index) - 10 - n
    
# Increase Permutation Method
# [n] indicate the permutation length
# for test, next = add 2, previous = subtract 2, p2index = add 20, index2p = subtract 20
# for test permutation length, more n variables base last step test
class Increase:
    
    # return the [current] permutation's next permutation 
    @staticmethod
    def next(n, current):
        #TODO
        return (int)(current) + 2 + n
    
    # return the [current] permutation's previous permutation 
    @staticmethod
    def previous(n, current):
        #TODO
        return (int)(current) - 2 - n
    
    # return the [current] permutation's index
    @staticmethod
    def index(n, current):
        #TODO
        return (int)(current) + 20 + n
    
    # return the [index] permutation
    @staticmethod
    def permutation(n, index):
        #TODO
        return (int)(index) - 20 - n
    
# Decrease Permutation Method
# [n] indicate the permutation length
# for test, next = add 3, previous = subtract 3, p2index = add 30, index2p = subtract 30
# for test permutation length, more n variables base last step test
class Decrease:
    
    # return the [current] permutation's next permutation 
    @staticmethod
    def next(n, current):
        #TODO
        return (int)(current) + 3 + n
    
    # return the [current] permutation's previous permutation 
    @staticmethod
    def previous(n, current):
        #TODO
        return (int)(current) - 3 - n 
    
    # return the [current] permutation's index
    @staticmethod
    def index(n, current):
        #TODO
        return (int)(current) + 30 + n
    
    # return the [index] permutation
    @staticmethod
    def permutation(n, index):
        #TODO
        return (int)(index) - 30 - n

# Switch Permutation Method
# [n] indicate the permutation length
# for test, next = add 4, previous = subtract 4, p2index = add 40, index2p = subtract 40
# for test permutation length, more n variables base last step test
class Switch:
    
    # return the [current] permutation's next permutation 
    @staticmethod
    def next(n, current):
        #TODO
        return (int)(current) + 4 + n
    
    # return the [current] permutation's previous permutation 
    @staticmethod
    def previous(n, current):
        #TODO
        return (int)(current) - 4 - n
    
    # return the [current] permutation's index
    @staticmethod
    def index(n, current):
        #TODO
        return (int)(current) + 40 + n
    
    # return the [index] permutation
    @staticmethod
    def permutation(n, index):
        #TODO
        return (int)(index) - 40 - n