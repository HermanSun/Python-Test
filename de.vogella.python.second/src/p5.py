'''
Created on Sep 23, 2016

@author: HermanSun
'''
class Rectangle(object):
    def __init__(self, h, w):
        self.it_height = h
        self.it_width = w
    def is_square(self):
        if self.it_height ==self.it_width:
            return True
        else:
            return False
    def diagonal_len(self):
        self.diagonalLen = (self.it_height**2+self.it_width**2)**0.5
        return self.diagonalLen
    def height(self):
        return self.it_height
    def width(self):
        return self.it_width
    def area(self):
        return self.it_width*self.it_height
    def perimeter(self):
        return 2*(self.it_width+self.it_height)
    
'''    
r1 = Rectangle(4,3)
print r1.is_square()
print r1.height()
print r1.width()
print r1.area()
print r1.perimeter()
print r1.diagonal_len()
'''



