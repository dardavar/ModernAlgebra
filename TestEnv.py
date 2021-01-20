import FFUtils
from FFElement import FFElement

print(FFUtils.SuperPower(83,11,101))
print(FFUtils.ExtendedEuclideanAlgorithm(25,804))

for i in range(0,7):
    a = FFElement(i)
    print("The add inverse of " + str(a.value) + " is " + str(a.AddInverse().value))
    print("The mul inverse of " + str(a.value) + " is " + str(a.MulInverse().value))
    print("The add order of "   + str(a.value) + " is " + str(a.AddOrder()))
    print("The mul order of "   + str(a.value) + " is " + str(a.MulOrder()))
    for j in range(0,7):
        b = FFElement(j)
        print(str(i) + " + " + str(j) + " = " + str(a.Add(b).value))
        print(str(i) + " - " + str(j) + " = " + str(a.Sub(b).value))
        print(str(i) + " * " + str(j) + " = " + str(a.Mul(b).value))
        print(str(i) + " / " + str(j) + " = " + str(a.Div(b).value))
    print("")
    print("")


