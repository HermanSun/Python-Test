'''
Created on Sep 25, 2016

@author: HermanSun
'''
class TextProcessor(object):
    def __init__(self, test_string):
        self._string = test_string
    def count_alphabet(self):
        i=0
        for a in self._string:
            if a.isalpha() :
                i=i+1
        return i
    def vowel_capitalization(self):
        it_string = self._string
        
        for i in range(len(self._string)):
            if self._string[i] in "AEIOUaeiou":
                it_string = it_string[:i]+it_string[i].upper()+it_string[i+1:]
        return it_string
    def concat(self, new_string):  
        return self._string+new_string
    def char_count(self):  
        t=list()
        for x in self._string:
            if (x,self._string.count(x)) not in t:
                t.append((x, self._string.count(x)))
               
        t.sort(cmp=None, key=None, reverse=False)
        return t
'''
k = "Alice was born in 1996. "   
tp = TextProcessor(k)
print tp.count_alphabet()
print tp.vowel_capitalization()
print tp.concat('She is 22 now. ')
print tp.char_count()
'''