"""Solution of Linear Congruences."""

import argparse

"""Insert code for extendedEuclid and linearCongruence here."""

def extendedEuclid(a: int, b: int):
    """returns gcd(a,b) and Bezout coefficients"""
    if b == 0:
        return(a, 1, 0)
    q, r = divmod(a, b)
    d, s, t = extendedEuclid(b, r)
    return d, t, s - q*t

def linearCongruence(a, b, m):
    d1, s1, t1 = extendedEuclid(a, m)
    if d1 != 1:
        print("a and m not relatively prime, ERROR")
        return
    x = (s1*b) % a
    return x


if __name__ == '__main__':
    # Parse command line.
    # By default, solve 3x congr. to 1 (mod 2)
    parser = argparse.ArgumentParser(
        description='Solver of linear congruences.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-v', '--verbose', help='increase output verbosity',
                        default=0, action='count')
    parser.add_argument('-l', '--lhs', help='left-hand side coefficient',
                        default=3, type=int)
    parser.add_argument('-r', '--rhs', help='right-hand side coefficient',
                        default=1, type=int)
    parser.add_argument('-m', '--mod', help='modulus for the congruence',
                        default=2, type=int)
    args = parser.parse_args()

    a = args.lhs
    b = args.rhs
    m = args.mod
    if args.verbose > 0:
        print('Solving', a, '* x =', b, '( mod', m, ')')
    solution = linearCongruence(a, b, m)
    if solution is None:
        print('no solution found')
    else:
        if (a*solution) % m != b % m:
            print('Wrong solution:', (a*solution) % m, '!=', b % m)
        print(solution, '+ k *', m)
