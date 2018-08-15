'''
Created on Oct 16, 2016

@author: HermanSun
'''
class Node(object):
    def __init__(self, v, n):
        self.value = v
        self.next = n

class LinkedList(object):
    def __init__(self):
        self.firstLink = None
    def add (self, newElement):
        self.firstLink = Node(newElement, self.firstLink)

    def test(self, testValue):
        
# your code here
    def remove(self, testValue):
# your code here
    def len(self): # return size of linked list
# your code here
    def reverse(self): # return reverse linked list
# your code here
    def Lprint(self):
# your code here