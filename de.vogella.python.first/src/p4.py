'''
Created on Sep 14, 2016

@author: HermanSun
'''
import random

x=random.randint(-100,100)

i=1
while True:
    y=input("Please input your guess: ")
    if y>x:
        print "Your guess is too high!"
    elif y<x:
        print "Your guess is too low!"
    else: 
        print"You are right after trying for ", i," times. Program ends."
        break    
    i+=1