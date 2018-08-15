'''
Created on Sep 23, 2016

@author: HermanSun
'''
def divisible_sublist(list1, d1, d2):
    list2=[]
    for a in list1:
        if a%d1==0 and a%d2==0:
            list2.append(a)
    
    return list2
#print divisible_sublist([653, 47281, 99, 10086,21,42,49,168,336], 3, 7)