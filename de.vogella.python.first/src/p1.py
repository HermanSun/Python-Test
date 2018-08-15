'''
Created on 2016.9.13

@author: HermanSun
'''
a = 0
#1st
while True:
    try:
        x = float(raw_input('Please input the first number: '))
        break
    except ValueError:
        print "Your input is not a number"
a = x

#2nd
while True:
    try:
        x = float(raw_input('Please input the second number: '))
        break
    except ValueError:
        print "Your input is not a number"
if x>a:
    a=x

#3nd
while True:
    try:
        x = float(raw_input('Please input the Third number: '))
        break
    except ValueError:
        print "Your input is not a number!"
if x>a:
    a=x
    
#4th
while True:
    try:
        x = float(raw_input('Please input the fourth number: '))
        break
    except ValueError:
        print "Your input is not a number"
if x>a:
    a=x
print "The largest value is ", a
