'''
Created on Oct 3, 2016

@author: HermanSun
'''

#a
a = range(1,11)
print map(lambda x:x**2, a)
print map(lambda x: x+1, a)

#b
print [x for x in a if x<=5]
print [x*x for x in a if x%2==0]