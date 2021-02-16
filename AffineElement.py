from FFElement import FFElement, DEFAULT_CHARACTERISTIC

class AffineElement:

    def __init__(self,affine_group, x, y):

        if(y.value != 0):
            self.x = x
        else: #The identity element
            self.x = FFElement(1,affine_group.p)
        
        self.y = y
        self.affine_group = affine_group

        if(y.value != 0 and y**2-x**3-affine_group.a*x-affine_group.b!=0):
            raise ValueError
    
    def __str__(self):
        if self.is_identity():
            return "INF"
        return f"({self.x}, {self.y})"
    
    def inverse(self):
        return AffineElement(self.affine_group,self.x,self.y.additive_inverse())
    
    def __eq__(self,other):
        return (self.x == other.x and self.y == other.y)

    #Computes P+Q = R
    def __add__(self,other):
        #if self is the identity element
        if self.is_identity():
            return other
        #if other is the identity element
        elif other.is_identity() == 0:
            return self
        elif self.inverse() == other:
            return self.affine_group.generate_identity_element()
        else:
            if (self==other):
                m = (FFElement(3,self.affine_group.p)*(self.x)^2 + self.affine_group.a)/(FFElement(2,self.affine_group.p)*self.y)
            else:
                m = ((other.y-self.y)/(other.x-self.x))
            x_R = m^2 - self.x - other.x
            y_R = m*(self.x-other.x) - self.y
            return AffineElement(self.affine_group, x_R, y_R)

    #returns nP
    def multiply_by_value(self,n):
        if n == 0:
            return self.affine_group.generate_identity_element()
        elif n % 2 == 1:
            return self + self.multiply_by_value(n - 1)
        else:
            a = self.multiply_by_value(n/2)
            return a + a 
    
    def calc_order(self):
        element_order = 0
        group_order = self.affine_group.order
        current_element = self
        while(element_order < group_order):
            element_order += 1
            if current_element.is_identity():
                break
            current_element = self + current_element
        return element_order

    def generate_subgroup(self):
        subgroup = []
        current_element = self
        while (not current_element.is_identity()):
            subgroup.append(current_element)
            current_element = self + current_element
        subgroup.append(self.affine_group.generate_identity_element())
        return subgroup
    
    def print_subgroup(self):
        subgroup = self.generate_subgroup()

        for element in subgroup:
            print(element)

    def is_identity(self):
        return self.x.value == 1 and self.y.value == 0
