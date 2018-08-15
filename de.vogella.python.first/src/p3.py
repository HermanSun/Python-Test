'''
Created on Sep 14, 2016

@author: HermanSun
'''
import math

def draw (c):
    ct = c*" "
    print ct+"*"

for i in range(361):
    a= i * math.pi / 180
    t = math.sin(a)
    k = (t+1)/2*80
    k = int(round(k))
    draw(k)
    