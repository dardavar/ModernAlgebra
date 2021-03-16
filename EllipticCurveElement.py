from FFElement import FFElement


class EllipticCurveElement:

    def __init__(self, group, X, Y, Z):
        self.X = FFElement(X, group.p)
        self.Y = FFElement(Y, group.p)
        self.Z = FFElement(Z, group.p)
        self.group = group

        if (Y ** 2) * Z != X ** 3 + group.a * X * Z ** 2 + group.b * Z ** 3:
            raise ValueError

    def __str__(self):
        return f"({self.X}, {self.Y}, {self.Z})"
