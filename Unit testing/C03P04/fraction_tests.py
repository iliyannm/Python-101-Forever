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
