# (c) Sandiway Fong, University of Arizona, 2022
from itertools import permutations
from nltk.tree import Tree
import sys
import re 
from nltk.corpus import ptb

mx = 0    
def dom(x, d): #d stands for depth - now i gotta change every other part of the code to match
    yield x, d
    depth = 0
    if not isinstance(x, str):
        for y in x:
            yield from dom(y, d+1)
          
    
count = 0    
def counter():
    global count
    for t in ptb.parsed_sents():
        cc(t)
    #print (count)   
    print (mx)
          
def cc(x):        
    if not isinstance(x, str):
        if len(x) > 1:
            for y,z in permutations(x, 2):
                for w, de in dom(z, 0):
                    w = re.search('^\*T\*-([0-9]+$)', str(w))
                    if w:
                        m = re.search('^WH.*-([0-9]+)', y.label())
                        if m:
                            if w.group(1) == m.group(1):
                                global count
                                global mx
                                count += 1
                                if de > mx:
                                    mx = de
                                    
            for u in x:
                cc(u)
                
        else:
            cc(x[0])
         

counter()