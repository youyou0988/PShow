# -*- coding: cp936 -*-
from globals.constants import OVERFLOW, ERROR, WARNING

# Dictionary Permutation Method
# [n] indicate the permutation length
# for test permutation type, next = add 1, previous = subtract 1, p2index = add 10, index2p = subtract 10
# for test permutation length, more n variables base last step test 
class Dictionary:
    const = [0,1,2,6,24,120,720,5040,40320,362800,3628000,39908000,478896000,6225648000,87159072000,1307386080000,20918177280000,355609013760000,6400962247680000,121618282705920000,2432365654118400000]
    # return the [current] permutation's next permutation 
    @staticmethod
    def next(n, current):
        #TODO
        idx,ans = index(n,current)
        if(idx=='fault'):
            return idx,ans
        ans = ans + 1
        idx,ans = permutation(n,ans)
        return idx,ans
    
    # return the [current] permutation's previous permutation 
    @staticmethod
    def previous(n, current):
        #TODO
        idx,ans = index(n,current)
        if(idx=='fault'):
            return idx,ans
        ans = ans - 1
        idx,ans = permutation(n,ans)
        return idx,ans
    
    # return the [current] permutation's index
    @staticmethod
    def index(n, current):
        #TODO
        if((n<1)|(n>20)):
            idx = 'fault'
            ans = 'n should between 1 and 20'
            return idx,ans
        if(len(current)!=n):
            idx = 'fault'
            ans = 'the length not match'
            return idx,ans
        ls = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n']
        lsn = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n']
        num = range(n)
        ans = 0
        idx = ''
        for i in range(n):       
            num[i] = 0
            for j in range(i,n):
                if(current[i]>current[j]):
                    num[i]=num[i]+1
            ans = ans + num[i]*const[n-i-1]
        for i in range(0,n-1):
            idx = idx + lsn[num[i]]
        return idx,ans
    
    # return the [index] permutation
    @staticmethod
    def permutation(n, index):
        #TODO
        if((n<1)|(n>20)):
            idx = 'fault'
            ans = 'n should between 1 and 20'
            return idx,ans
        if((index<0)|(index>=const[n])):
            idx = 'fault'
            ans = 'index should between 0 and n！-1'
        ls = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n']
        lsn = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n']
        num = range(n-1,-1,-1)
        res = range(n)
        result = ''
        idx = ''
        for i in range(0,n-1):
            # num[i] = index/const[n-i-1]
            # index = index%const[n-i-1]
	    val = index/const[n-i-1]
	    num[i] = val
	    index = index%const[n-i-1]
        for i in range(0,n):
            result = result+(ls[num[i]])
            ls.remove(ls[num[i]])
	for i in range(0,n-1):
	    idx = idx + lsn[num[i]]
        return result
    
# Increase Permutation Method
# [n] indicate the permutation length
# for test, next = add 2, previous = subtract 2, p2index = add 20, index2p = subtract 20
# for test permutation length, more n variables base last step test
class Increase:
    const = [0,1,2,6,24,120,720,5040,40320,362800,3628000,39908000,478896000,6225648000,87159072000,1307386080000,20918177280000,355609013760000,6400962247680000,121618282705920000,2432365654118400000]
    # return the [current] permutation's next permutation 
    @staticmethod
    def next(n, current):
        #TODO
        idx,ans = index(n,current)
        if(idx=='fault'):
            return idx,ans
        ans = ans + 1
        idx,ans = permutation(n,ans)
        return idx,ans
    
    # return the [current] permutation's previous permutation 
    @staticmethod
    def previous(n, current):
        #TODO
        idx,ans = index(n,current)
        if(idx=='fault'):
            return idx,ans
        ans = ans - 1
        idx,ans = permutation(n,ans)
        return idx,ans
    
    # return the [current] permutation's index
    @staticmethod
    def index(n, current):
        #TODO
        if((n<1)|(n>20)):
            idx = 'fault'
            ans = 'n should between 1 and 20'
            return idx,ans
        if(len(current)!=n):
            idx = 'fault'
            ans = 'the length not match'
            return idx,ans
        ls = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n']
        lsn = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n']
        num = range(n)
        ans = 0
        idx = ''
        for i in range(n):
            ss = current[i]
            val = n - lsn.index(ss)
            num[val] = 0
            for j in range(i,n):
                if(current[i]>scurrent[j]) : num[val]=num[val]+1
            ans = ans + num[val]*const[n-val-1]
        for i in range(0,n-1):
            idx = idx + lsn[num[i]]
        return idx,ans
    
    # return the [index] permutation
    @staticmethod
    def permutation(n, index):
        #TODO
        if((n<1)|(n>20)):
            idx = 'fault'
            ans = 'n should between 1 and 20'
            return idx,ans
        if((index<0)|(index>=const[n])):
            idx = 'fault'
            ans = 'index should between 0 and n！-1'
        ls = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n']
        lsn = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n']
        num = range(n-1,-1,-1)
        res = range(n)
        used = range(n)
        result = ''
        idx = ''
        for i in range(0,n-1):
            num[i] = index/const[n-i-1]
            index = index%const[n-i-1]        
        pos = range(n-1,-1,-1)
        for i in range(n):
            res[pos[num[i]]]=n-i
            pos.remove(pos[num[i]])
        for i in range(n):
            result = result + lsn[res[i]]
        for i in range(0,n-1):
            idx = idx + lsn[num[i]]
        return idx,result
    
# Decrease Permutation Method
# [n] indicate the permutation length
# for test, next = add 3, previous = subtract 3, p2index = add 30, index2p = subtract 30
# for test permutation length, more n variables base last step test
class Decrease:
    const = [0,1,2,6,24,120,720,5040,40320,362800,3628000,39908000,478896000,6225648000,87159072000,1307386080000,20918177280000,355609013760000,6400962247680000,121618282705920000,2432365654118400000]
    # return the [current] permutation's next permutation 
    @staticmethod
    def next(n, current):
        #TODO
        idx,ans = index(n,current)
        if(idx=='fault'):
            return idx,ans
        ans = ans + 1
        idx,ans = permutation(n,ans)
        return idx,ans
    
    # return the [current] permutation's previous permutation 
    @staticmethod
    def previous(n, current):
        #TODO
        idx,ans = index(n,current)
        if(idx=='fault'):
            return idx,ans
        ans = ans - 1
        idx,ans = permutation(n,ans)
        return idx,ans
    
    # return the [current] permutation's index
    @staticmethod
    def index(n, current):
        #TODO
        if((n<1)|(n>20)):
            idx = 'fault'
            ans = 'n should between 1 and 20'
            return idx,ans
        if(len(current)!=n):
            idx = 'fault'
            ans = 'the length not match'
            return idx,ans
        ls = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n']
        lsn = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n']
        num = range(n)
        ans = 0
        idx = ''
        for i in range(n):
            ss = current[i]
            val = n - lsn.index(ss)
            num[val] = 0
            for j in range(i,n):
                if(current[i]>current[j]) : num[val]=num[val]+1       
        for j in range(0,n-1):
            ans = ans*(j+2)+num[j+1]
        for i in range(n-2,-1,-1):
            idx = idx + lsn[num[i]]
        return idx,ans
    
    # return the [index] permutation
    @staticmethod
    def permutation(n, index):
        #TODO
        if((n<1)|(n>20)):
            idx = 'fault'
            ans = 'n should between 1 and 20'
            return idx,ans
        if((index<0)|(index>=const[n])):
            idx = 'fault'
            ans = 'index should between 0 and n！-1'
        ls = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n']
        lsn = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n']
        num = range(n-1,-1,-1)
        res = range(n)
        used = range(n)
        result = ''
        idx = ''
        for i in range(n):
            num[n-i-1] = index%(n-i)
            index = index/(n-i)        
        pos = range(n-1,-1,-1)
        for i in range(n):
            res[pos[num[n-1-i]]]=n-i
            pos.remove(pos[num[n-1-i]])
        for i in range(n):
            result = result + lsn[res[i]]
        for i in range(1,n):
            idx = idx + lsn[num[i]]
        return idx,result

# Switch Permutation Method
# [n] indicate the permutation length
# for test, next = add 4, previous = subtract 4, p2index = add 40, index2p = subtract 40
# for test permutation length, more n variables base last step test
class Switch:
    const = [0,1,2,6,24,120,720,5040,40320,362800,3628000,39908000,478896000,6225648000,87159072000,1307386080000,20918177280000,355609013760000,6400962247680000,121618282705920000,2432365654118400000]
    # return the [current] permutation's next permutation 
    @staticmethod
    def next(n, current):
        #TODO
        idx,ans = index(n,current)
        if(idx=='fault'):
            return idx,ans
        ans = ans + 1        
        idx,ans = permutation(n,ans)
        return idx,ans
    
    # return the [current] permutation's previous permutation 
    @staticmethod
    def previous(n, current):
        #TODO
        idx,ans = index(n,current)
        if(idx=='fault'):
            return idx,ans
        ans = ans - 1
        idx,ans = permutation(n,ans)
        return idx,ans
    
    # return the [current] permutation's index
    @staticmethod
    def index(n, current):
        #TODO
        if((n<1)|(n>20)):
            idx = 'fault'
            ans = 'n should between 1 and 20'
            return idx,ans
        if(len(current)!=n):
            idx = 'fault'
            ans = 'the length not match'
            return idx,ans
        ls = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n']
        lsn = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n']
        num = range(n)
        ans = 0
        idx = ''
        for i in range(n):
            num[i] = 0
        num[1] = 1
        for j in range(2,n):
            ##val = s.find(str(j+1))
            val = current.find(ls[j])
            if(j%2==0):
                if(num[j-1]%2==0):
                    for k in range(val,n):
                        if(current[k]<current[val]): num[j]=num[j]+1
                if(num[j-1]%2==1):
                    for k in range(0,val):
                        if(current[k]<current[val]): num[j]=num[j]+1
            if(j%2==1):
                if((num[j-2]+num[j-1])%2==0):
                    for k in range(val,n):
                        if(current[k]<current[val]): num[j]=num[j]+1
                if((num[j-2]+num[j-1])%2==1):
                    for k in range(0,val):
                        if(current[k]<current[val]): num[j]=num[j]+1
        for j in range(0,n-1):
            ans = ans*(j+2)+num[j+1]
        for i in range(1,n):
            idx = idx + lsn[num[i]]
        return idx,ans
    
    # return the [index] permutation
    @staticmethod
    def permutation(n, index):
        #TODO
        if((n<1)|(n>20)):
            idx = 'fault'
            ans = 'n should between 1 and 20'
            return idx,ans
        if((index<0)|(index>=const[n])):
            idx = 'fault'
            ans = 'index should between 0 and n！-1'
        ls = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n']
        lsn = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n']
        num = range(n-1,-1,-1)
        res = range(n)
        used = range(n)
        result = ''
        idx = ''
        for i in range(n):
            res[i]=0
            num[n-i-1] = index%(n-i)
            index = index/(n-i)        
        pos = range(n-1,-1,-1)
        for i in range(n-1,1,-1):
            if(i%2==1):
                if((num[i-1]+num[i-2])%2==1):
                    res[pos[i-num[i]]]=i+1
                    pos.remove(pos[i-num[i]])
                if((num[i-1]+num[i-2])%2==0):
                    res[pos[num[i]]]=i+1
                    pos.remove(pos[num[i]])
            if(i%2==0):
                if(num[i-1]%2==1):
                    res[pos[i-num[i]]]=i+1
                    pos.remove(pos[i-num[i]])
                if(num[i-1]%2==0):
                   res[pos[num[i]]]=i+1
                   pos.remove(pos[num[i]])
            if(num[1]==0):
                res[pos[0]]=2
                res[pos[1]]=1
            if(num[1]==1):
                res[pos[0]]=1
                res[pos[1]]=2
        for i in range(1,n):
            idx = idx + lsn[num[i]]
        for i in range(n):
            result = result + lsn[res[i]]
        return idx,result
