'''
Created on Oct 16, 2016

@author: HermanSun
'''
import sys
input_filename = sys.argv[1]
output_filename = sys.argv[2]
try:
    f = open(input_filename)
except IOError,e:
    sys.exit('No matching!')
k = f.readlines()
f.close()
f1 = open(output_filename,"w")
char =0
for i in f1:
    for j in i:
        char=char + 1 
f1.write('Number of characters: '+ char+'\n')
count_word = 0
for i in f1:
    for word in i:
        count_word +=1
f1.write('Number of words: '+ count_word+'\n')
f1.write('Number of lines: '+ len(f1)+'\n')

