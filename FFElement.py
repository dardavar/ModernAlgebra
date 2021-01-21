import FFUtils

class FFElement:

    def __init__(self, value, characteristic=7):
        self.value = value
        self.characteristic = characteristic
    
    def AddInverse(self):
        if(self.value==0):
            return FFElement(0)
        return FFElement(self.characteristic - self.value)
    
    def MulInverse(self):
        try:
            if(self.value == 0):
                raise ZeroDivisionError
            return FFElement(FFUtils.ExtendedEuclideanAlgorithm(self.value, self.characteristic)[1])          
        except ZeroDivisionError:
            print ("Zero have no inverse, returning -1")
            return FFElement(-1)
    
    def AddOrder(self):
        if(self.value==0):
            return 1
        return self.characteristic

    def Add(self, other):
        return FFElement((self.value + other.value) % self.characteristic)
    
    def Sub(self, other):
        return FFElement((self.value + other.AddInverse().value) % self.characteristic)
    
    def Mul(self, other):
        return FFElement((self.value * other.value) % self.characteristic)
    
    #get the multlipical inverse and multiply by it
    def Div(self, other):
        return self.Mul(other.MulInverse())

    def AddPower(self,power):
        return FFElement((self.value*power)%self.characteristic)

    def MulPower(self,power):
        return FFElement(FFUtils.SuperPower(self.value, power, self.characteristic-1))
    
    def MulOrder(self, special = True):
        #define o(0) as -1
        if(self.value==0):
            return -1
        elif(self.value==1):
            return 1
        if (self.Mul(self).value==1):
                return 2    
        #if (p-1)/2 is prime, then its the only number needs to be checked
        elif(special):
            if((self.MulPower((self.characteristic-1)/2)).value==1):
                return (self.characteristic-1)/2
        #if (p-1)/2 isn't prime, check every divisor of (p-1)/2
        else:
            for i in range(2,self.characteristic):
                if(self.characteristic%i==0):
                    if (self.MulPower(i).value==1):
                        return i
        return self.characteristic - 1
            

    

        
