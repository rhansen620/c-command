# (c) Sandiway Fong, University of Arizona, 2022
from itertools import permutations
from nltk.tree import Tree
import sys
import re
from nltk.corpus import ptb

i=0
def dom(x, path):
    if path is None:
        path = list()
    yield x, path
    if not isinstance(x, str):
        path.append(x.label())
        for y in x:
            yield from dom(y, path.copy())
total = 0
def cc(x):
    global i
    global total
    if not isinstance(x, str):
        if len(x) > 1:
            for y,z in permutations(x, 2):
                m1 = re.search(r'^NP.*', y.label())
                if m1:
                    for w, path in dom(z, None):
                        if isinstance(w, str):
                            m2 = re.search(r'[a-zA-Z].*self$', w)
                        else:
                            m2 = re.search(r'\w[a-zA-Z]*self$', w.label())
                        if m2:
                            print('tree',i, ':',y, 'c-commands', w, 'path', path)
                            #i+70000, right after the 'tree',
                            total +=1
                            
            for u in x:
                cc(u)
        else:
            cc(x[0])
            
smallptb = ptb.parsed_sents() [70000:73451]
for t in smallptb:
    cc(t)
    i+=1
print (total)
   

#if len(sys.argv) == 2:
 #   with open(sys.argv[1]) as f:
 #       t  = Tree.fromstring(f.read())
 #       cc(t)
 #   print (total)
#