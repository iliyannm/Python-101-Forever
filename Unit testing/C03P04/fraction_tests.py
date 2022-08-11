from unittest import TestCase
from fraction import Fraction


class DummyFraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator


class FractionTests(TestCase):
    def test_init(self):
        with self.subTest('Happy cases'):
            fraction = Fraction(1, 2)

            self.assertEqual(1, fraction.numerator)
            self.assertEqual(2, fraction.denominator)

        with self.subTest('Denominator is 0'):
            with self.assertRaises(ValueError):
                Fraction(1, 0)

    def test_str(self):
        cases = [
            (Fraction(1, 2), "1/2"),
            (Fraction(1, 1), "1/1"),
            (Fraction(2, 1), "2/1"),
            (Fraction(2, 4), "2/4"),
            (Fraction(0, 1), "0"),
        ]

        for obj, expected in cases:
            with self.subTest(f'Expected: {expected}'):
                self.assertEqual(expected, str(obj))

    def test_repr(self):
        cases = [
            (Fraction(1, 2), "Fraction(1, 2)"),
            (Fraction(1, 1), "Fraction(1, 1)"),
            (Fraction(2, 1), "Fraction(2, 1)"),
            (Fraction(2, 4), "Fraction(2, 4)"),
            (Fraction(0, 1), "Fraction(0, 1)"),
        ]

        for obj, expected in cases:
            with self.subTest(f'Expected: {expected}'):
                self.assertEqual(expected, repr(obj))

    def test_eq(self):
        with self.subTest('Happy cases'):
            a = Fraction(1, 2)
            b = Fraction(1, 2)
            c = Fraction(1, 3)

            self.assertEqual(a, b)
            self.assertEqual(b, a)

            self.assertNotEqual(a, c)
            self.assertNotEqual(c, a)

            self.assertNotEqual(b, c)
            self.assertNotEqual(c, b)

        with self.subTest('Fractions are equal even unsimplified'):
            a = Fraction(1, 2)
            b = Fraction(2, 4)

            self.assertEqual(a, b)
            self.assertEqual(b, a)

        with self.subTest('Fractions with zero are equal'):
            a = Fraction(0, 1)
            b = Fraction(0, 2)

            self.assertEqual(a, b)
            self.assertEqual(b, a)

        with self.subTest('Fractions are not equal to other Fraction`s classes'):
            a = Fraction(1, 2)
            b = DummyFraction(1, 2)

            self.assertRaises(TypeError)
            self.assertRaises(TypeError)

    def test_add(self):
        with self.subTest('Same denominator'):
            a = Fraction(1, 2)
            b = Fraction(3, 2)

            expected = Fraction(4, 2)

            self.assertEqual(expected, a + b)
            self.assertEqual(expected, b + a)

        with self.subTest('Different denominator'):
            a = Fraction(3, 4)
            b = Fraction(4, 5)

            expected = Fraction(31, 20)

            self.assertEqual(expected, a + b)
            self.assertEqual(expected, b + a)

        with self.subTest('Zero'):
            a = Fraction(4, 5)
            b = Fraction(0, 3)

            expected = Fraction(4, 5)

            self.assertEqual(expected, a + b)
            self.assertEqual(expected, b + a)

        with self.subTest('DummyFraction'):
            a = Fraction(4, 5)
            b = DummyFraction(3, 4)

            with self.assertRaises(TypeError):
                a + b

    def test_sub(self):
        with self.subTest('Same denominator'):
            a = Fraction(1, 2)
            b = Fraction(3, 2)

            a_minus_b_expected = Fraction(-2, 2)
            b_minus_a_expected = Fraction(2, 2)

            self.assertEqual(a_minus_b_expected, a - b)
            self.assertEqual(b_minus_a_expected, b - a)

        with self.subTest('Different denominator'):
            a = Fraction(3, 4)
            b = Fraction(4, 5)

            a_minus_b_expected = Fraction(-1, 20)
            b_minus_a_expected = Fraction(1, 20)

            self.assertEqual(a_minus_b_expected, a - b)
            self.assertEqual(b_minus_a_expected, b - a)

        with self.subTest('Zero'):
            a = Fraction(4, 5)
            b = Fraction(0, 3)

            a_minus_b_expected = Fraction(12, 15)
            b_minus_a_expected = Fraction(-12, 15)

            self.assertEqual(a_minus_b_expected, a - b)
            self.assertEqual(b_minus_a_expected, b - a)

        with self.subTest('DummyFraction'):
            a = Fraction(4, 5)
            b = DummyFraction(3, 4)

            with self.assertRaises(TypeError):
                a - b

    def test_multiply(self):
        with self.subTest('Happy cases'):
            a = Fraction(4, 5)
            b = Fraction(3, 4)

            expected = Fraction(12, 20)

            self.assertEqual(expected, a * b)
            self.assertEqual(expected, b * a)

        with self.subTest('Zero'):
            a = Fraction(4, 5)
            b = Fraction(0, 4)

            expected = Fraction(0, 17)

            self.assertEqual(expected, a * b)
            self.assertEqual(expected, b * a)

        with self.subTest('One'):
            a = Fraction(4, 5)
            b = Fraction(1, 1)

            expected = Fraction(4, 5)

            self.assertEqual(expected, a * b)
            self.assertEqual(expected, b * a)

        with self.subTest('Unsimplified one'):
            a = Fraction(4, 5)
            b = Fraction(2, 2)

            expected = Fraction(8, 10)

            self.assertEqual(expected, a * b)
            self.assertEqual(expected, b * a)

        with self.subTest('DummyFraction'):
            a = Fraction(4, 5)
            b = DummyFraction(3, 4)

            with self.assertRaises(TypeError):
                a * b

    def test_simplification(self):
        with self.subTest('Simplified fractions are simplified'):
            a = Fraction(1, 2)
            simplified = a.simplify()

            self.assertEqual(a, simplified)
            self.assertTrue(a.is_simplified())
            self.assertTrue(simplified.is_simplified())

            self.assertEqual(a.numerator, simplified.numerator)
            self.assertEqual(a.denominator, simplified.denominator)

        with self.subTest('Can simplify fraction'):
            a = Fraction(2, 4)
            simplified = a.simplify()

            self.assertEqual(a, simplified)

            self.assertFalse(a.is_simplified())
            self.assertTrue(simplified.is_simplified())

            self.assertEqual(1, simplified.numerator)
            self.assertEqual(2, simplified.denominator)

        with self.subTest('Zero'):
            a = Fraction(0, 3)
            simplified = a.simplify()

            self.assertEqual(a, simplified)
            self.assertTrue(a.is_simplified())
            self.assertTrue(simplified.is_simplified())

            self.assertEqual(a.numerator, simplified.numerator)
            self.assertEqual(a.denominator, simplified.denominator)