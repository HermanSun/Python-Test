'''
Created on Sep 14, 2016

@author: HermanSun
'''
a = raw_input("Please input a string: ")
while True:
    b=a[::-1]
    if b!=a:
        a=raw_input("No. Please input another string: \n")
    else: 
        print "Yes. Program ends."
        break
