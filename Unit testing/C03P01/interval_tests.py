from unittest import TestCase
from interval import Interval


class IntervalTests(TestCase):
    def test_start_is_not_closed_and_end_is_not_closed(self):
        closed_interval = Interval(1, 10)
        self.assertTrue(closed_interval.is_inside(1))
        self.assertTrue(closed_interval.is_inside(5))
        self.assertTrue(closed_interval.is_inside(10))
        self.assertEqual("[1, 10]", closed_interval.stringify())

    def test_start_is_closed_and_end_is_closed(self):
        opened_interval = Interval(1, 10, start_opened=True, end_opened=True)
        self.assertFalse(opened_interval.is_inside(1))
        self.assertTrue(opened_interval.is_inside(5))
        self.assertFalse(opened_interval.is_inside(10))
        self.assertEqual("(1, 10)", opened_interval.stringify())

    def test_start_is_not_closed_and_end_is_closed(self):
        half_opened_interval = Interval(1, 10, start_opened=False, end_opened=True)
        self.assertTrue(half_opened_interval.is_inside(1))
        self.assertTrue(half_opened_interval.is_inside(5))
        self.assertFalse(half_opened_interval.is_inside(10))
        self.assertEqual("[1, 10)", half_opened_interval.stringify())

    def test_start_is_closed_and_end_is_not_closed(self):
        half_opened_interval = Interval(1, 10, start_opened=True, end_opened=False)
        self.assertFalse(half_opened_interval.is_inside(1))
        self.assertTrue(half_opened_interval.is_inside(5))
        self.assertTrue(half_opened_interval.is_inside(10))
        self.assertEqual("(1, 10]", half_opened_interval.stringify())
