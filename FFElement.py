import FFUtils

DEFAULT_CHARACTERISTIC = 179


class FFElement:
    def __init__(self, value, characteristic=DEFAULT_CHARACTERISTIC):
        self.value = value % characteristic
        self.characteristic = characteristic

    def __add__(self, other):
        return FFElement((self.value + other.value) % self.characteristic, self.characteristic)

    def __sub__(self, other):
        return FFElement((self.value + other.additive_inverse().value) % self.characteristic, self.characteristic)

    def __mul__(self, other):
        return FFElement((self.value * other.value) % self.characteristic, self.characteristic)

    # get the multiplication inverse and multiply by it
    def __truediv__(self, other):
        try:
            if other.value == 0:
                raise ZeroDivisionError
        except ZeroDivisionError:
            print("Can not divide by 0, returning -1")
            return -1
        return self * (other.multiplication_inverse())

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return repr(self.__class__.__name__ + f"({self.value},{self.characteristic})")

    def __eq__(self, other):
        return self.value == other.value and self.characteristic == other.characteristic

    def additive_inverse(self):
        if self.value == 0:
            return FFElement(0)

        return FFElement(self.characteristic - self.value, self.characteristic)

    def multiplication_inverse(self):
        try:
            if self.value == 0:
                raise ZeroDivisionError
            return FFElement(FFUtils.extended_euclidean_algorithm(self.value, self.characteristic)[1],
                             self.characteristic)
        except ZeroDivisionError:
            print("Zero have no inverse, returning -1")
            return -1

    def additive_order(self):
        if self.value == 0:
            return 1
        return self.characteristic

    def additive_power(self, power):
        return FFElement((self.value * power) % self.characteristic, self.characteristic)

    def __pow__(self, power):
        return FFElement(FFUtils.super_power(self.value, power, self.characteristic), self.characteristic)

    def multiplication_order(self, special=True):
        # define o(0) as -1
        # if P is safe, than P-1 = 2q => O(a) in {1, 2 , q , p-1}, this is due to the fact that the order must divide
        # p-1 and the prime factorization is unique.
        if self.value == 0:
            return -1

        elif self.value == 1:
            return 1

        if (self * self).value == 1:
            return 2

            # if (p-1)/2 is prime, then its the only number needs to be checked
        elif special:
            if (self ** ((self.characteristic - 1) / 2)).value == 1:
                return (self.characteristic - 1) / 2

        # if (p-1)/2 isn't prime, check every divisor of (p-1)/2
        else:
            for i in range(3, (self.characteristic - 1) // 2 + 1):
                if ((self.characteristic - 1) % i) == 0:
                    if (self ** i).value == 1:
                        return i
        return self.characteristic - 1
