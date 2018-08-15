'''
Created on Sep 23, 2016

@author: HermanSun
'''
def list_mul(list1, list2):
    rlist=[]
    a = len(list1)+len(list2)-1
    #print a
    for i2 in range(len(list2)):
        for i in range(a):
            if i < len(rlist):
                continue
            i1=i-i2
          
            if i1>=len(list1):
                break
            #print i, i1, i2 #for check number
            k=list1[i1]
            j=list2[i2]
            w=k*j
            rlist.append(w)
            #print rlist
            if a==len(rlist):
                return rlist


'''
a1 = [1,3,5]
a2 = [2,4]
print list_mul(a1, a2)
'''