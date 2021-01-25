import FFUtils
from FFElement import FFElement

print(FFUtils.SuperPower(83, 11, 101))
print(FFUtils.ExtendedEuclideanAlgorithm(25, 804))

for i in range(0, 7):
    a = FFElement(i)
    print("The add inverse of " + str(a.value) + " is " + str(a.add_inverse().value))
    print("The mul inverse of " + str(a.value) + " is " + str(a.mul_inverse().value))
    print("The add order of " + str(a.value) + " is " + str(a.add_order()))
    print("The mul order of " + str(a.value) + " is " + str(a.mul_order()))
    for j in range(0, 7):
        b = FFElement(j)
        print(str(i) + " + " + str(j) + " = " + str(a.add(b).value))
        print(str(i) + " - " + str(j) + " = " + str(a.sub(b).value))
        print(str(i) + " * " + str(j) + " = " + str(a.mul(b).value))
        print(str(i) + " / " + str(j) + " = " + str(a.div(b).value))
    print("")
    print("")
