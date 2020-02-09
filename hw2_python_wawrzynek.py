#ouput:
# a: False (knave)
# b: False (knave)
# solution not unique

from z3 import *

def block_model(s):
    m = s.model()
    return [a != m[a]]

def print_model(s):
    m = s.model()
    
    print('a:', m[a])
    print('b:', m[b])


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


a, b = [Bool(name) for name in ['a', 'b']]

s = Solver()
s.add(Implies(a, Xor(a, b)))

solve_and_print(s)

