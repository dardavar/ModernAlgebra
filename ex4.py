from FFElement import FFElement, DEFAULT_CHARACTERISTIC


def solver(coefficient_a, coefficient_b, p=DEFAULT_CHARACTERISTIC):
    """Find a,b from Fp which solve the expression (coefficient_a*a**3 + coefficient_b+b**2 !=0)mod p"""
    coefficient_a = FFElement(coefficient_a, p)
    coefficient_b = FFElement(coefficient_b, p)

    for i in range(2, p):
        for j in range(2, p):
            a = FFElement(i)
            b = FFElement(j)
            if (coefficient_a * (a ** 3) + coefficient_b * (b ** 2)).value != 0:
                break

    print(f"a is {a} and b is {b}")


if __name__ == '__main__':
    solver(4, 27)
