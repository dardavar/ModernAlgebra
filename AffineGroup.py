import math
from EllipticCurveGroup import EllipticCurveGroup
from FFElement          import FFElement, DEFAULT_CHARACTERISTIC
from AffineElement      import AffineElement

class AffineGroup:

    def __init__(self,elliptic_curve):

        self.a = elliptic_curve.a
        self.b = elliptic_curve.b
        self.p = elliptic_curve.p
        self.order = len(self.generate_all_points())
    
    def print_all_points(self):
        points = self.generate_all_points()
        for point in points:
            print(point)
    
    def generate_all_points(self):
        points = []
        points.append(self.generate_identity_element())
        for x_value in range(0,self.p):
            x = FFElement(x_value,self.p)
            y_square = FFElement(x**3+self.a*x+self.b)

            for y_value in range(0,self.p):
                y = FFElement(y_value,self.p)
                if y**2==y_square:
                    point = AffineElement(self,x,y)
                    points.append(point)
                    break         
        return points

    def check_hasse_theorem(self):
        all_points_size = len(self.generate_all_points())

        if abs(all_points_size-(self.p+1)) <= 2*math.sqrt(self.p):
            print(f"The bound is hold! (N={all_points_size+1}, q={self.p})")
        else:
            print("The bound does not hold! Congratz! You have break the math!")
    
    def generate_identity_element(self):
        AffineElement(self,FFElement(1,self.p),FFElement(0,self.p))
        
    