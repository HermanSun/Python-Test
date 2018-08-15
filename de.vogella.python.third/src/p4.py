'''
Created on Oct 3, 2016

@author: HermanSun
'''
def quicksort(a):
    if len(a)<=1:
        return  [x for x in a]
    else:  middlekey = a[len(a)/2]
    middle = [x for x in a if x==middlekey]
    smaller = quicksort([x for x in a if x<middlekey])
    larger = quicksort([x for x in a if x>middlekey])
    lst = []
    lst.extend(smaller)
    lst.extend(middle)
    lst.extend(larger)    
    return [x for x in lst]
'''
lst = [2,2,3,4,555,6,3,4,5,7,1,2,4]
print quicksort(lst)
'''