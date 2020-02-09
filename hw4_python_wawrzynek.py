#ouput:
# v: False (which means v is NOT guilty)
# W: False (which means w is NOT guilty)
# solution not unique

import sys
from z3 import *

if len(sys.arv) > 2:
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


