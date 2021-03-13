from FFElement import FFElement, DEFAULT_CHARACTERISTIC
from EllipticCurveElement import EllipticCurveElement
from AffineGroup import AffineGroup
from AffineElement import AffineElement
class EllipticCurveGroup:

    def __init__(self, a=178, b=2, p=DEFAULT_CHARACTERISTIC):
        
        self.a = FFElement(a,p)
        self.b = FFElement(b,p)
        self.p = p
        
        if FFElement(4,p)*(self.a**3)+FFElement(27,p)*(self.b**2) == FFElement(0,p):
            raise ValueError
    
    def generate_identity_element(self):
        return EllipticCurveElement(self,0,1,0) 
    
    def group_order(self):
        return AffineGroup(self).order
