import math
from FFElement import FFElement
from AffineElement import AffineElement


class AffineGroup:

    # Class of affine group, each object consist of a, b and the field finite number characteristic
    def __init__(self, elliptic_curve):
        self.a = elliptic_curve.a
        self.b = elliptic_curve.b
        self.p = elliptic_curve.p
        self.order = len(self.generate_all_points())

    # print all group supportive points
    def print_all_points(self):
        points = self.generate_all_points()
        for point in points:
            print(point)

    # generate list of the group supportive points which holds the equation of y^2=x^3+a*x+b
    def generate_all_points(self):
        points = [self.generate_identity_element()]
        for x_value in range(0, self.p):
            x = FFElement(x_value, self.p)
            y_square = x ** 3 + self.a * x + self.b

            for y_value in range(0, self.p):
                y = FFElement(y_value, self.p)
                if y ** 2 == y_square:
                    point = AffineElement(self, x, y)
                    points.append(point)
        return points

    def check_hasse_theorem(self):
        all_points_size = len(self.generate_all_points())
        return abs(all_points_size - (self.p + 1)) <= 2 * math.sqrt(self.p)

    def generate_identity_element(self):
        return AffineElement(self, FFElement(0, self.p), FFElement(1, self.p))
