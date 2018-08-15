'''
Created on Oct 4, 2016

@author: HermanSun
'''
def word_count(x,n):
    str1 = filter(lambda y: len(y)>=n, x)
      
    return reduce(lambda x,y: x+y, [x.count("python") for x in str1])

'''
x=['python python python pythom python','python is boring', 'python is a large hevay-bodied snake', 'the pythodn course is worse taking']
print word_count(x, 20)
'''