from FFElement import FFElement


def solver():
    x = FFElement(4, 7)
    y = FFElement(27, 7)
    a = FFElement(2)
    b = FFElement(2)
    while (x * (a ** 3) + y * (b ** 2)).value == 0:
        a = a + FFElement(1)
        b = b + FFElement(1)
    print(f"a is {a} and b is {b}")


if __name__ == '__main__':
    solver()
