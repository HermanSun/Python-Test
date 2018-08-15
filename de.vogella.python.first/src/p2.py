'''
Created on Sep 14, 2016

@author: HermanSun
'''

def drawGraph(a,str):
    #for i in range(a) :
    print str*a 
        # i+=1
    return 0; 
while True :
    b = input('Enter an integer: ')
    if b == -1:
        print 'Program ends.'
        False
        break
    str = raw_input('Enter a string: ')

    for i in range(b):
        a= i+1
        drawGraph(a,str)
    print "\n"

         
