'''
Created on Sep 20, 2016

@author: HermanSun
'''
def recursive_pow(x,n):
    if n == 0:
        value=1
    elif n%2==0:
        value = recursive_pow(x, n/2)*recursive_pow(x, n/2)
    elif n%2==1:
        value = x*recursive_pow(x, n-1)
    return value
'''
while True:
    x,n=input('2 integers')
    if n==-1:
        break
    print recursive_pow (x,n)
'''