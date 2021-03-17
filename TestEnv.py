import unittest
import FFUtils
from FFElement import FFElement
from EllipticCurveGroup import EllipticCurveGroup
from AffineGroup import AffineGroup
from AffineElement import AffineElement


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
        self.assertEqual(EllipticCurveGroup(6, 2, 7).group_order(), 9)
        self.assertEqual(EllipticCurveGroup(10, 3, 11).group_order(), 17)


class TestAffineGroup(unittest.TestCase):
    def test_inverse(self):
        elliptic_curve = EllipticCurveGroup(6, 2, 7)
        affine_group = AffineGroup(elliptic_curve)
        self.assertEqual(AffineElement(affine_group, FFElement(2, 7), FFElement(6, 7)).inverse(),
                         AffineElement(affine_group, FFElement(2, 7), FFElement(1, 7)))
        self.assertEqual(AffineElement(affine_group, FFElement(6, 7), FFElement(3, 7)).inverse(),
                         AffineElement(affine_group, FFElement(6, 7), FFElement(4, 7)))
        self.assertEqual(AffineElement(affine_group, FFElement(1, 7), FFElement(0, 7)).inverse(),
                         AffineElement(affine_group, FFElement(1, 7), FFElement(0, 7)))

    def test_addition(self):
        elliptic_curve = EllipticCurveGroup(6, 2, 7)
        affine_group = AffineGroup(elliptic_curve)
        self.assertEqual(
            AffineElement(affine_group, FFElement(1, 7), FFElement(0, 7)) + AffineElement(affine_group, FFElement(6, 7),
                                                                                          FFElement(3, 7)),
            AffineElement(affine_group, FFElement(6, 7), FFElement(3, 7)))
        self.assertEqual(
            AffineElement(affine_group, FFElement(6, 7), FFElement(3, 7)) + AffineElement(affine_group, FFElement(6, 7),
                                                                                          FFElement(4, 7)),
            AffineElement(affine_group, FFElement(1, 7), FFElement(0, 7)))
        self.assertEqual(
            AffineElement(affine_group, FFElement(6, 7), FFElement(3, 7)) + AffineElement(affine_group, FFElement(6, 7),
                                                                                          FFElement(3, 7)),
            AffineElement(affine_group, FFElement(6, 7), FFElement(4, 7)))
        self.assertEqual(
            AffineElement(affine_group, FFElement(6, 7), FFElement(3, 7)) + AffineElement(affine_group, FFElement(2, 7),
                                                                                          FFElement(6, 7)),
            AffineElement(affine_group, FFElement(0, 7), FFElement(3, 7)))

    def test_element_order(self):
        elliptic_curve = EllipticCurveGroup(6, 2, 7)
        affine_group = AffineGroup(elliptic_curve)
        self.assertEqual(AffineElement(affine_group, FFElement(2, 7), FFElement(6, 7)).calc_order(), 9)
        self.assertEqual(AffineElement(affine_group, FFElement(6, 7), FFElement(3, 7)).calc_order(), 3)
        self.assertEqual(AffineElement(affine_group, FFElement(1, 7), FFElement(0, 7)).calc_order(), 1)

    def test_power(self):
        elliptic_curve = EllipticCurveGroup(6, 2, 7)
        affine_group = AffineGroup(elliptic_curve)
        self.assertEqual(AffineElement(affine_group, FFElement(6, 7), FFElement(3, 7)).multiply_by_value(0),
                         affine_group.generate_identity_element())
        self.assertEqual(AffineElement(affine_group, FFElement(6, 7), FFElement(3, 7)).multiply_by_value(1),
                         AffineElement(affine_group, FFElement(6, 7), FFElement(3, 7)))
        self.assertEqual(AffineElement(affine_group, FFElement(6, 7), FFElement(3, 7)).multiply_by_value(5),
                         AffineElement(affine_group, FFElement(6, 7), FFElement(4, 7)))

    def test_hasse_thm(self):
        elliptic_curve = EllipticCurveGroup(6, 2, 7)
        self.assertTrue(AffineGroup(elliptic_curve).check_hasse_theorem())

        EllipticCurveGroup(10, 3, 11)
        self.assertTrue(AffineGroup(elliptic_curve).check_hasse_theorem())

        elliptic_curve = EllipticCurveGroup()
        self.assertTrue(AffineGroup(elliptic_curve).check_hasse_theorem())
    
    def tomer_tests_group_order(self):
        self.assertEqual(AffineGroup(EllipticCurveGroup(12, 0, 83)).order,84)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,0, 83)).order,84)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,1, 83)).order,77)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,2, 83)).order,70)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,3, 83)).order,70)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,4, 83)).order,68)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,5, 83)).order,99)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,6, 83)).order,79)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,7, 83)).order,84)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,8, 83)).order,75)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,9, 83)).order,95)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,10, 83)).order,87)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,11, 83)).order,72)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,12, 83)).order,82)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,13, 83)).order,74)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,14, 83)).order,92)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,15, 83)).order,75)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,16, 83)).order,75)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,17, 83)).order,87)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,18, 83)).order,77)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,19, 83)).order,88)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,20, 83)).order,78)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,21, 83)).order,78)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,22, 83)).order,75)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,23, 83)).order,78)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,24, 83)).order,87)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,25, 83)).order,72)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,26, 83)).order,79)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,27, 83)).order,72)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,28, 83)).order,72)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,29, 83)).order,80)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,30, 83)).order,98)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,31, 83)).order,76)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,32, 83)).order,88)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,33, 83)).order,84)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,34, 83)).order,90)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,35, 83)).order,70)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,36, 83)).order,95)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,37, 83)).order,96)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,38, 83)).order,100)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,39, 83)).order,80)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,40, 83)).order,92)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,41, 83)).order,84)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,42, 83)).order,84)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,43, 83)).order,76)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,44, 83)).order,88)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,45, 83)).order,68)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,46, 83)).order,72)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,47, 83)).order,73)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,48, 83)).order,98)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,49, 83)).order,78)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,50, 83)).order,84)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,51, 83)).order,80)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,52, 83)).order,92)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,53, 83)).order,70)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,54, 83)).order,88)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,55, 83)).order,96)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,56, 83)).order,96)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,57, 83)).order,89)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,58, 83)).order,96)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,59, 83)).order,81)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,60, 83)).order,90)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,61, 83)).order,93)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,62, 83)).order,90)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,63, 83)).order,90)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,64, 83)).order,80)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,65, 83)).order,91)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,66, 83)).order,81)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,67, 83)).order,93)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,68, 83)).order,93)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,69, 83)).order,76)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,70, 83)).order,94)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,71, 83)).order,86)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,72, 83)).order,96)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,73, 83)).order,81)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,74, 83)).order,73)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,75, 83)).order,93)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,76, 83)).order,84)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,77, 83)).order,89)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,78, 83)).order,69)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,79, 83)).order,100)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,80, 83)).order,98)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,81, 83)).order,98)
        self.assertEqual(AffineGroup(EllipticCurveGroup(12,82, 83)).order,91)
    
    def tomer_tests_element_order(self):
        group = AffineGroup(EllipticCurveGroup(12,25, 83))
        self.assertEqual(AffineElement(group,FFElement(0, 83),FFElement(1, 83)),1)
        self.assertEqual(AffineElement(group,FFElement(0, 83),FFElement(5, 83)),36)
        self.assertEqual(AffineElement(group,FFElement(0, 83),FFElement(78, 83)),36)
        self.assertEqual(AffineElement(group,FFElement(1, 83),FFElement(11, 83)),24)
        self.assertEqual(AffineElement(group,FFElement(1, 83),FFElement(72, 83)),24)
        self.assertEqual(AffineElement(group,FFElement(5, 83),FFElement(25, 83)),72)
        self.assertEqual(AffineElement(group,FFElement(5, 83),FFElement(58, 83)),72)
        self.assertEqual(AffineElement(group,FFElement(6, 83),FFElement(8, 83)),72)
        self.assertEqual(AffineElement(group,FFElement(6, 83),FFElement(75 ,83)),72)
        self.assertEqual(AffineElement(group,FFElement(7, 83),FFElement(28 ,83)),9)
        self.assertEqual(AffineElement(group,FFElement(7, 83),FFElement(55 ,83)),9)
        self.assertEqual(AffineElement(group,FFElement(11, 83),FFElement( 34,83)),24)
        self.assertEqual(AffineElement(group,FFElement(11, 83),FFElement( 49,83)),24)
        self.assertEqual(AffineElement(group,FFElement(15, 83),FFElement( 29,83)),72)
        self.assertEqual(AffineElement(group,FFElement(15, 83),FFElement( 54,83)),72)
        self.assertEqual(AffineElement(group,FFElement(20, 83),FFElement( 31,83)),36)
        self.assertEqual(AffineElement(group,FFElement(20, 83),FFElement( 52,83)),36)
        self.assertEqual(AffineElement(group,FFElement(22, 83),FFElement( 8 ,83)),12)
        self.assertEqual(AffineElement(group,FFElement(22, 83),FFElement( 75,83)),12)
        self.assertEqual(AffineElement(group,FFElement(24, 83),FFElement( 39,83)),4)
        self.assertEqual(AffineElement(group,FFElement(24, 83),FFElement( 44,83)),4)
        self.assertEqual(AffineElement(group,FFElement(26, 83),FFElement( 20,83)),24)
        self.assertEqual(AffineElement(group,FFElement(26, 83),FFElement( 63,83)),24)
        self.assertEqual(AffineElement(group,FFElement(27, 83),FFElement( 19,83)),9)
        self.assertEqual(AffineElement(group,FFElement(27, 83),FFElement( 64,83)),9)
        self.assertEqual(AffineElement(group,FFElement(28, 83),FFElement( 22,83)),18)
        self.assertEqual(AffineElement(group,FFElement(28, 83),FFElement( 61,83)),18)
        self.assertEqual(AffineElement(group,FFElement(29, 83),FFElement( 32,83)),3)
        self.assertEqual(AffineElement(group,FFElement(29, 83),FFElement( 51,83)),3)
        self.assertEqual(AffineElement(group,FFElement(30, 83),FFElement( 24,83)),72)
        self.assertEqual(AffineElement(group,FFElement(30, 83),FFElement( 59,83)),72)
        self.assertEqual(AffineElement(group,FFElement(31, 83),FFElement( 15,83)),72)
        self.assertEqual(AffineElement(group,FFElement(31, 83),FFElement( 68,83)),72)
        self.assertEqual(AffineElement(group,FFElement(33, 83),FFElement( 2 ,83)), 72)
        self.assertEqual(AffineElement(group,FFElement(33, 83),FFElement( 81,83)), 72)
        self.assertEqual(AffineElement(group,FFElement(34, 83),FFElement( 35,83)), 9)
        self.assertEqual(AffineElement(group,FFElement(34, 83),FFElement( 48,83)), 9)
        self.assertEqual(AffineElement(group,FFElement(35, 83),FFElement( 34,83)), 72)
        self.assertEqual(AffineElement(group,FFElement(35, 83),FFElement( 49,83)), 72)
        self.assertEqual(AffineElement(group,FFElement(37, 83),FFElement( 34,83)), 18)
        self.assertEqual(AffineElement(group,FFElement(37, 83),FFElement( 49,83)), 18)
        self.assertEqual(AffineElement(group,FFElement(38, 83),FFElement( 18,83)), 8)
        self.assertEqual(AffineElement(group,FFElement(38, 83),FFElement( 65,83)), 8)
        self.assertEqual(AffineElement(group,FFElement(42, 83),FFElement( 0 ,83)), 2)
        self.assertEqual(AffineElement(group,FFElement(43, 83),FFElement( 6 ,83)),18)
        self.assertEqual(AffineElement(group,FFElement(43, 83),FFElement( 77,83)),18)
        self.assertEqual(AffineElement(group,FFElement(44, 83),FFElement( 9 ,83)), 8)
        self.assertEqual(AffineElement(group,FFElement(44, 83),FFElement( 74,83)), 8)
        self.assertEqual(AffineElement(group,FFElement(47, 83),FFElement( 9 ,83)), 72)
        self.assertEqual(AffineElement(group,FFElement(47, 83),FFElement( 74,83)),72)
        self.assertEqual(AffineElement(group,FFElement(49, 83),FFElement( 30,83)),6)
        self.assertEqual(AffineElement(group,FFElement(49, 83),FFElement( 53,83)),6)
        self.assertEqual(AffineElement(group,FFElement(55, 83),FFElement( 8 ,83)),72)
        self.assertEqual(AffineElement(group,FFElement(55, 83),FFElement( 75,83)), 72)
        self.assertEqual(AffineElement(group,FFElement(56, 83),FFElement( 41,83)), 72)
        self.assertEqual(AffineElement(group,FFElement(56, 83),FFElement( 42,83)), 72)
        self.assertEqual(AffineElement(group,FFElement(57, 83),FFElement( 27,83)), 72)
        self.assertEqual(AffineElement(group,FFElement(57, 83),FFElement( 56,83)), 72)
        self.assertEqual(AffineElement(group,FFElement(58, 83),FFElement( 6 ,83)), 36)
        self.assertEqual(AffineElement(group,FFElement(58, 83),FFElement( 77,83)), 36)
        self.assertEqual(AffineElement(group,FFElement(59, 83),FFElement( 40,83)), 12)
        self.assertEqual(AffineElement(group,FFElement(59, 83),FFElement( 43,83)), 12)
        self.assertEqual(AffineElement(group,FFElement(61, 83),FFElement( 22,83)), 24)
        self.assertEqual(AffineElement(group,FFElement(61, 83),FFElement( 61,83)), 24)
        self.assertEqual(AffineElement(group,FFElement(65, 83),FFElement( 6 ,83)),36)
        self.assertEqual(AffineElement(group,FFElement(65, 83),FFElement( 77,83)),36)
        self.assertEqual(AffineElement(group,FFElement(75, 83),FFElement( 9 ,83)),36)
        self.assertEqual(AffineElement(group,FFElement(75, 83),FFElement( 74,83)),36)
        self.assertEqual(AffineElement(group,FFElement(77, 83),FFElement( 22,83)),72)
        self.assertEqual(AffineElement(group,FFElement(77, 83),FFElement( 61,83)),72)
        self.assertEqual(AffineElement(group,FFElement(82, 83),FFElement( 26,83)),36)
        self.assertEqual(AffineElement(group,FFElement(82, 83),FFElement( 57,83)),36)

if __name__ == '__main__':
    unittest.main()
