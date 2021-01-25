# computes a^b mod n efficiently
def SuperPower(a, b, n):
    if b == 0:
        return 1
    elif b % 2 == 1:
        return a * SuperPower(a, b - 1, n) % n
    else:
        a = SuperPower(a, b / 2, n)
        return (a * a) % n


# returns the gcd of a and b, and x, y s.t. gcd(a,b)=x*a+y*b.
def ExtendedEuclideanAlgorithm(a, b):
    if (a == 0):
        return b, 0, 1
    gcd, x1, y1 = ExtendedEuclideanAlgorithm(b % a, a)

    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y
