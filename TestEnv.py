import unittest

import FFUtils
from FFElement import FFElement


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

    def test_curve(self):
        for i in range(0,179):
            self.assertNotEqual(FFElement(i,179)**3+FFElement(178,179)*FFElement(i,179)+FFElement(2,179),FFElement(0,179))


if __name__ == '__main__':
    unittest.main()
