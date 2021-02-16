from FFElement import FFElement, DEFAULT_CHARACTERISTIC
from EllipticCurveElement import EllipticCurveElement
from AffineGroup import AffineGroup

class EllipticCurveGroup:

    def __init__(self, a=178, b=2, p=DEFAULT_CHARACTERISTIC):
        
        self.a = FFElement(a,p)
        self.b = FFElement(b,p)
        self.p = p
        
        if FFElement(4,p)*(a**3)+FFElement(27,p)*(b**2) == 0:
            raise ValueError
    
    def generate_identity_element(self):
        return EllipticCurveElement(self,0,1,0) 
    
    def group_order(self):
        print("The order of the group is: " + str(AffineGroup(self).order))


