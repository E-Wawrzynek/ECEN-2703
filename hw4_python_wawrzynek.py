#ouput:

from z3 import *
import sys
import math

def block_model(s):
    m = s.model()
    return Or([v != m[v] for v in x])

def print_model(s):
    m = s.model()
    print(' '.join([str(m[v]) for v in x]))

if len(sys.argv) > 2:
    raise SystemExit("There should be at most one argument")
elif len(sys.argv) == 2:
    try:
        N = int(sys.argv[1])
    except:
        raise SystemExit("N should be an integer")
    if N < 0:
        raise SystemExit("N should be non-negative")
else:
    N = 15 #default value

x = [Int('x%s', i) for i in range(1, N+1, 1)]
sqr = []
s = Solver()

for m in range(2*N+1):
    sqr.append(m*m)

for num in x:
    num >= 1
    num <= N

Distinct(num)

for k in range(1, N):
    for j in range(len(sqr)):
        num[k] + num[k+1] == sqr[j]  

print(num)