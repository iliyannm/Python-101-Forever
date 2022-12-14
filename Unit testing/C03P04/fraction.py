from math import gcd, lcm


class Fraction:
    def __init__(self, numerator, denominator):
        """
        Construct a new Fraction.

        If denominator = 0, raise ValueError.
        """
        self.numerator = numerator
        self.denominator = denominator

        if self.denominator == 0:
            raise ValueError('Denominator can not be 0')

    def __str__(self):
        """
        Returns the string representation of self.
        """
        if self.numerator == 0:
            return "0"

        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        """
        Returns the REPL representation of self.
        """

        return f"Fraction({self.numerator}, {self.denominator})"

    def __eq__(self, other):
        """
        Returns True/False, if _self is equal to _other.
        """
        if not isinstance(other, Fraction):
            raise TypeError(f"{other} is not equal to Fracion")

        self_gcd = gcd(self.numerator, self.denominator)
        other_gcd = gcd(other.numerator, other.denominator)

        return (self.numerator // self_gcd == other.numerator // other_gcd
                and
                self.denominator // self_gcd == other.denominator // other_gcd)

    def __add__(self, other):
        """
        Returns new Fraction, that's the sum of self and other.
        """
        if not isinstance(other, Fraction):
            raise TypeError(f"{other} is not equal to Fracion")

        self_lcm = lcm(self.denominator, other.denominator) // self.denominator
        other_lcm = lcm(self.denominator, other.denominator) // other.denominator

        return Fraction(
            self.numerator * self_lcm + other.numerator * other_lcm,
            lcm(self.denominator, other.denominator)
        )

    def __sub__(self, other):
        """
        Returns new Fraction, that's the substraction of self and other.
        """
        if not isinstance(other, Fraction):
            raise TypeError(f"{other} is not equal to Fracion")

        self_lcm = lcm(self.denominator, other.denominator) // self.denominator
        other_lcm = lcm(self.denominator, other.denominator) // other.denominator

        return Fraction(
            self.numerator * self_lcm - other.numerator * other_lcm,
            lcm(self.denominator, other.denominator)
        )

    def __mul__(self, other):
        """
        Returns new Fraction, that's the product of self and other.
        """
        if not isinstance(other, Fraction):
            raise TypeError(f"{other} is not equal to Fracion")

        return Fraction(
            self.numerator * other.numerator,
            self.denominator * other.denominator
        )

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError(f"{other} is not equal to Fracion")

        self_lcm = lcm(self.denominator, other.denominator) // self.denominator
        other_lcm = lcm(self.denominator, other.denominator) // other.denominator

        return self_lcm * self.numerator < other_lcm * other.numerator

    def simplify(self):
        """
        Returns new Fraction, that's the simplification of self
        """
        if self.numerator == 0:
            return Fraction(self.numerator, self.denominator)

        self_gcd = gcd(self.numerator, self.denominator)

        return Fraction(
            self.numerator // self_gcd,
            self.denominator // self_gcd
        )

    def is_simplified(self):
        """
        Returns True/False, if self cannot be simplified further
        """
        return self.numerator == 0 or gcd(self.numerator, self.denominator) == 1
