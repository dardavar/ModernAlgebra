# computes a^b mod n efficiently
def super_power(a, b, n):
    if b == 0:
        return 1
    elif b % 2 == 1:
        return a * super_power(a, b - 1, n) % n
    else:
        a = super_power(a, b / 2, n)
        return (a * a) % n


# returns the gcd of a and b, and x, y s.t. gcd(a,b)=x*a+y*b.
def extended_euclidean_algorithm(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_euclidean_algorithm(b % a, a)

    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y
