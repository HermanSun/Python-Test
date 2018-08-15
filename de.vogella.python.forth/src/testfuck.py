import sys

if len(sys.argv)<3:
    sys.exit('Not enough arguments!')
   
a = sys.argv[1]
b = sys.argv[2]

try: 
    f= open(b)
except IOError, e:
    print 'File does not exist!'
lst = f.readlines()
lst1 = []
for i in lst:
    if a.lower() in i.lower():
        lst1.append(i)
file.close()
if lst1==[]:
    print sys.exit('No match!')
for i in lst1:
    print i,
print ' end'
