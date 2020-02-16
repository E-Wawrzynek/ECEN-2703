#output:


from z3 import *

def check_validity(sentence):
    s = Solver()
    s.add(Not(sentence))
    result = s.check
    if result == sat:
        print("Not valid. Model for the negation:")
        print_model(s.model())
    elif result == unsat:
        print('Valid.')
    else:
        print('Unable to solve.')

def print_model(s):
    m = s.model()
    print('v:', m[v])


x = Int('x')
y = Int('y')
z = Int('z')

sentence = ForAll([x], And((x < y), ForAll([z], Or(x >= z, z >= y))))

check_validity(sentence)


