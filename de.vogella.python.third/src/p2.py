'''
Created on Oct 3, 2016

@author: HermanSun
'''
#(a)
class Box(object):
    def __init__(self, ival):
        self.value = ival
    def __cmp__(self, other):
        if self.value < other.value:
            return -1
        elif self.value ==other.value:
            return 0
        elif self.value> other.value:
            return 1
    def __add__(self, other):
        a = self.value + other.value
        return Box(a)
    

'''
#(a) test
print Box(2)< Box(2) 
print Box(2)<=Box(2)
print Box(1)>=Box(2)
print Box(3)> Box(2)
print Box(0) ==Box(1)
print Box(0) != Box(0)
print Box(0) <> Box(0)
   
#print Box(2).value+Box(1).value      
#(b)
#print Box(2)+Box(1)
print (Box(1) + Box(2)).value
'''
   