import unittest
import math
import FFUtils
from FFElement            import FFElement, DEFAULT_CHARACTERISTIC
from EllipticCurveGroup   import EllipticCurveGroup
from EllipticCurveElement import EllipticCurveElement
from AffineGroup          import AffineGroup
from AffineElement        import AffineElement

class TestFFEElement(unittest.TestCase):

    def test_super_power(self):
        self.assertEqual(FFUtils.super_power(83, 11, 101), 42)
        self.assertEqual(FFUtils.super_power(83, 32, 88), 25)

    def test_extended_euclidean_algorithm(self):
        self.assertEqual(FFUtils.extended_euclidean_algorithm(25, 804), (1, 193, -6))
        self.assertEqual(FFUtils.extended_euclidean_algorithm(35, 375), (5, -32, 3))

    def test_additive_order(self):
        self.assertEqual(FFElement(3).additive_order(), 179)
        self.assertEqual(FFElement(11, 17).additive_order(), 17)

    def test_additive_inverse(self):
        self.assertEqual(FFElement(3).additive_inverse(), FFElement(176))
        self.assertEqual(FFElement(11, 17).additive_inverse(), FFElement(6, 17))

    def test_multiplication_inverse(self):
        self.assertEqual(FFElement(3).multiplication_inverse(), FFElement(60))
        self.assertEqual(FFElement(9, 17).multiplication_inverse(), FFElement(2, 17))

    def test_additive_power(self):
        self.assertEqual(FFElement(3).additive_power(3), FFElement(9))
        self.assertEqual(FFElement(5, 11).additive_power(3), FFElement(4, 11))

    def test_multiplication_order(self):
        self.assertEqual(FFElement(3, 17).multiplication_order(special=False), 16)
        self.assertEqual(FFElement(89, 179).multiplication_order(), 89)

    def test_multiplication_power(self):
        self.assertEqual(FFElement(3, 8) ** 4, FFElement(1, 8))
        self.assertEqual(FFElement(89, 179) ** 5, FFElement(151, 179))

    def test_multiplication(self):
        self.assertEqual(FFElement(2) * FFElement(5), FFElement(10))
        self.assertEqual(FFElement(3, 11) * FFElement(6, 11), FFElement(7, 11))

    def test_division(self):
        self.assertEqual(FFElement(2) / FFElement(5), FFElement(72))
        self.assertEqual(FFElement(72, 11) / FFElement(6, 11), FFElement(1, 11))

    def test_addition(self):
        self.assertEqual(FFElement(2) + FFElement(5), FFElement(7))
        self.assertEqual(FFElement(9, 11) + FFElement(6, 11), FFElement(4, 11))

    def test_subtraction(self):
        self.assertEqual(FFElement(2) - FFElement(5), FFElement(176))
        self.assertEqual(FFElement(9, 11) - FFElement(6, 11), FFElement(3, 11))

class TestEllipticCurveGroup(unittest.TestCase):
    def test_order(self):
        self.assertEqual(EllipticCurveGroup(6,2,7).group_order(),9)
        self.assertEqual(EllipticCurveGroup(10,3,11).group_order(),17)

class TestAffineGroup(unittest.TestCase):
    def test_inverse(self):
        elliptic_curve = EllipticCurveGroup(6,2,7)
        affine_group = AffineGroup(elliptic_curve)
        self.assertEqual(AffineElement(affine_group,FFElement(2,7),FFElement(6,7)).inverse(),AffineElement(affine_group,FFElement(2,7),FFElement(1,7)))
        self.assertEqual(AffineElement(affine_group,FFElement(6,7),FFElement(3,7)).inverse(),AffineElement(affine_group,FFElement(6,7),FFElement(4,7)))
        self.assertEqual(AffineElement(affine_group,FFElement(1,7),FFElement(0,7)).inverse(),AffineElement(affine_group,FFElement(1,7),FFElement(0,7)))
    
    def test_addition(self):
        elliptic_curve = EllipticCurveGroup(6,2,7)
        affine_group = AffineGroup(elliptic_curve)
        self.assertEqual(AffineElement(affine_group,FFElement(1,7),FFElement(0,7))+AffineElement(affine_group,FFElement(6,7),FFElement(3,7)), AffineElement(affine_group,FFElement(6,7),FFElement(3,7)))
        self.assertEqual(AffineElement(affine_group,FFElement(6,7),FFElement(3,7))+AffineElement(affine_group,FFElement(6,7),FFElement(4,7)), AffineElement(affine_group,FFElement(1,7),FFElement(0,7)))
        self.assertEqual(AffineElement(affine_group,FFElement(6,7),FFElement(3,7))+AffineElement(affine_group,FFElement(6,7),FFElement(3,7)), AffineElement(affine_group,FFElement(6,7),FFElement(4,7)))
        self.assertEqual(AffineElement(affine_group,FFElement(6,7),FFElement(3,7))+AffineElement(affine_group,FFElement(2,7),FFElement(6,7)), AffineElement(affine_group,FFElement(0,7),FFElement(3,7)))
    
    def test_element_order(self):
        elliptic_curve = EllipticCurveGroup(6,2,7)
        affine_group = AffineGroup(elliptic_curve)
        self.assertEqual(AffineElement(affine_group,FFElement(2,7),FFElement(6,7)).calc_order(),9)
        self.assertEqual(AffineElement(affine_group,FFElement(6,7),FFElement(3,7)).calc_order(),3)
        self.assertEqual(AffineElement(affine_group,FFElement(1,7),FFElement(0,7)).calc_order(),1)
    
    def test_power(self):
        elliptic_curve = EllipticCurveGroup(6,2,7)
        affine_group = AffineGroup(elliptic_curve)
        self.assertEqual(AffineElement(affine_group,FFElement(6,7),FFElement(3,7)).multiply_by_value(0),affine_group.generate_identity_element())
        self.assertEqual(AffineElement(affine_group,FFElement(6,7),FFElement(3,7)).multiply_by_value(1),AffineElement(affine_group,FFElement(6,7),FFElement(3,7)))
        self.assertEqual(AffineElement(affine_group,FFElement(6,7),FFElement(3,7)).multiply_by_value(5),AffineElement(affine_group,FFElement(6,7),FFElement(4,7)))
    
    def test_hasse_thm(self):
        elliptic_curve = EllipticCurveGroup(6,2,7)
        self.assertTrue(AffineGroup(elliptic_curve).check_hasse_theorem())

        EllipticCurveGroup(10,3,11)
        self.assertTrue(AffineGroup(elliptic_curve).check_hasse_theorem())

        elliptic_curve = EllipticCurveGroup()
        self.assertTrue(AffineGroup(elliptic_curve).check_hasse_theorem())

if __name__ == '__main__':
    unittest.main()
