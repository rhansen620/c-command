# (c) Sandiway Fong, University of Arizona, 2022
from itertools import permutations
from nltk.tree import Tree
import sys
import re 
from nltk.corpus import ptb

def dom(x):
    yield x
    if not isinstance(x, str):
        for y in x:
            yield from dom(y)
    
count = 0   
i=0 
def counter():
    global count
    for t in ptb.parsed_sents()RANGE:
        cc(t)
        i+=1
    print (count)   
          
def cc(x): 
    global i
    if not isinstance(x, str):
        if len(x) > 1:
            for y,z in permutations(x, 2):
                for w in dom(z):
                    w = re.search('^\*T\*-([0-9]+$)', str(w))
                    if w:
                        m = re.search('^WH.*-([0-9]+)', y.label())
                        if m:
                            if w.group(1) == m.group(1):
                                global count
                                count += 1
                                    
            for u in x:
                cc(u)
                
        else:
            cc(x[0])
         

counter()