#ouput:
# v: False (which means v is NOT guilty)
# W: False (which means w is NOT guilty)
# solution not unique

from z3 import *

def block_model(s):
    m = s.model()
    return Or([n != m[n] for n in [v, w]])

def print_model(s):
    m = s.model()
    
    print('v:', m[v])
    print('w:', m[w])


def solve_and_print(s):
    result = s.check()
    if result == sat:
        print_model(s)
        if s.check(block_model(s)) == unsat:
            print('unique solution')
        else:
            print('solution not unique')
    elif result == unsat:
        print('unsatisfiable constraints')
    else:
        print('unable to solve')

#a-h means "is a knight"
a, b, c, d, e, f, g, h = [Bool(name) for name in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']]
#v-w means "is guilty"
v, w = [Bool(name) for name in ['v', 'w']]

s = Solver()

s.add(a)
s.add(Implies(c, Not(a)))
s.add(Implies(d, Not(b)))
s.add(Implies(e, And(c, d)))
s.add(Implies(f, Or(a, b)))
s.add(Implies(g, Xor(And(e, f), And(Not(e), Not(f)))))
s.add(Implies(h, And(Xor(And(g, h), And(Not(g), Not(h))), Not(And(v, w)))))

solve_and_print(s)

