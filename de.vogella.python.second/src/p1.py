'''
Created on Sep 20, 2016

@author: HermanSun
'''
def roman_number(n):
    roman_string = ''
    if n>9999:
        print "Number is out of range."
        n=9999
    
    n1 = n%10 #000_
    n2 = n/10%10  #00_0 
    n3 = n/100%10 #0_00
    n4 = n/1000%10 #_000
    
    roman_string +=n4*'M'
    if n3<=3:
        roman_string += n3*'C'
    elif n3==4:
        roman_string += 'CD'
    elif n3>=5 and n3<=8:
        roman_string += 'D'+ 'C'*(n3-5)
    elif n3 == 9:
        roman_string += 'CM'
    
    if n2<=3:
        roman_string += n2*'X'
    elif n2==4:
        roman_string += 'XL'
    elif n2>=5 and n2<=8:
        roman_string += 'L'+'X'*(n2-5)
    elif n2==9:
        roman_string += 'XC'    
    
    
    if n1==1:
        roman_string += 'I'
    elif n1==2:
        roman_string += 'II'
    elif n1==3:
        roman_string += 'III'
    elif n1==4:
        roman_string += 'IV'
    elif n1==5:
        roman_string += 'V'
    elif n1==6:
        roman_string += 'VI'
    elif n1==7:
        roman_string += 'VII'
    elif n1==8:
        roman_string += 'VIII'
    elif n1==9:
        roman_string += 'IX'
        
    
    return roman_string

while True:
    n=input('an integer')
    if n==-1:
        break
    print roman_number(n)
