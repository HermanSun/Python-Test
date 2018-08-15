'''
Created on Oct 3, 2016

@author: HermanSun
'''
def is_key_unique(dict):
    key_value = dict.values()
    for i in key_value:
        if key_value.count(i)>=2:
            return False
    return True

'''      
d = {'a':1, 'b':2, 'c':3} #true
c = {'d':2, 'a':1, 'b':2, 'c':3}#false
a = {'a':1, 'b':2, 'c':3, 'd':2}#false
print 'd', is_key_unique(d)
print 'c', is_key_unique(c)
print 'a', is_key_unique(a)
'''