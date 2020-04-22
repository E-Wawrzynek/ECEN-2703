# output for k = 4 is 84

from z3 import Solver, Int, And, Or, ArithRef, BoolRef, sat, Not

from typing import Sequence, Collection

Graph = Sequence[Collection[int]]
VarList = Sequence[ArithRef]

def  Chromatic(G: Graph, k:int): #-> Optional[Coloring ]:
    """ Finds k-coloring  of G."""
    n = len(G)
    v = [Int('v%i' % i) for i in range(n)]
    s = Solver ()
    s.add([And(x>=0, x<k) for x in v])
    for i in range(n):
        s.add([v[i] != v[j] for j in G[i]])
    
    cnt = 0
    while s.check() == sat:
        cnt += 1
        m = s.model()
        s.add(Not(And([v[i] == m[v[i]] for i in range (n)])))
    return cnt

Gr = [
    {1,3},
    {0,2},
    {1,3},
    {2,0}
]

for i in range(9):
    num = Chromatic(Gr, i)
    print("The possible ways to color a square with k =", i,"is", num)