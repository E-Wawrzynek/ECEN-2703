# output:
# first 12-digit prime found is:
# 749669676277 from estring[53:65]

from sympy import isprime
from mpmath import mp
 
decimalPlaces = 100
with mp.workdps(decimalPlaces):
     estring = str(mp.e).replace('.','')
     
#print(estring)


for i in range(len(estring)+1):
    n = int(estring[i:i+12])
    m = isprime(n)
    if m is True:
        print("first 12-digit prime found is:")
        print(n, "from estring[%d:%d]" % (i, i+12))
        break
    elif i == len(estring):
        print('none found')