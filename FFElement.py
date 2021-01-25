import FFUtils

DEFAULT_PRIME = 7


class FFElement:
    def __init__(self, value, characteristic=DEFAULT_PRIME):
        self.value = value
        self.characteristic = characteristic

    def add_inverse(self):
        if self.value == 0:
            return FFElement(0)

        return FFElement(self.characteristic - self.value)

    def mul_inverse(self):
        try:
            if self.value == 0:
                raise ZeroDivisionError
            return FFElement(FFUtils.ExtendedEuclideanAlgorithm(self.value, self.characteristic)[1])
        except ZeroDivisionError:
            print("Zero have no inverse, returning -1")
            return FFElement(-1)

    def add_order(self):
        if self.value == 0:
            return 1
        return self.characteristic

    def add(self, other):
        return FFElement((self.value + other.value) % self.characteristic)

    def sub(self, other):
        return FFElement((self.value + other.add_inverse().value) % self.characteristic)

    def mul(self, other):
        return FFElement((self.value * other.value) % self.characteristic)

    # get the multlipical inverse and multiply by it
    def div(self, other):
        return self.mul(other.mul_inverse())

    def add_power(self, power):
        return FFElement((self.value * power) % self.characteristic)

    def mul_power(self, power):
        return FFElement(FFUtils.SuperPower(self.value, power, self.characteristic - 1))

    def mul_order(self, special=True):
        # define o(0) as -1
        if self.value == 0:
            return -1

        elif self.value == 1:
            return 1

        if self.mul(self).value == 1:
            return 2

            # if (p-1)/2 is prime, then its the only number needs to be checked
        elif special:
            if (self.mul_power((self.characteristic - 1) / 2)).value == 1:
                return (self.characteristic - 1) / 2

        # if (p-1)/2 isn't prime, check every divisor of (p-1)/2
        else:
            for i in range(2, self.characteristic):
                if self.characteristic % i == 0:
                    if self.mul_power(i).value == 1:
                        return i
        return self.characteristic - 1
