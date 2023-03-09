# (c) Sandiway Fong, University of Arizona, 2022
from itertools import permutations
from nltk.tree import Tree
import sys
import re 

def dom(x):
    yield x
    if not isinstance(x, str):
        for y in x:
            yield from dom(y)
            
def cc(x):
    if not isinstance(x, str):
        if len(x) > 1:
            for y,z in permutations(x, 2):
                for w in dom(z):
                    w = re.search('^\*T\*-([0-9]+$)', str(w))
                    if w:
                        m = re.search('^WH.*-([0-9]+)', y.label())
                        if m:
                            if w.group(1) == m.group(1):
                                print(y, 'c-commands', w.string)
            for u in x:
                cc(u)
        else:
            cc(x[0])

if len(sys.argv) == 2:
    with open(sys.argv[1]) as f:
        t  = Tree.fromstring(f.read())
        cc(t)
