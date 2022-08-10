from unittest import TestCase
from exception_silencing import ExceptionSilencer


class ExceptionSilencerTests(TestCase):
    def test_exception_can_be_silenced(self):
        with ExceptionSilencer(ValueError):
            int('aa')

    def test_exception_can_be_silenced_with_nested_managers(self):
        with ExceptionSilencer(ValueError):
            with ExceptionSilencer(Exception):
                int('aa')

    def test_exception_is_raised(self):
        with self.assertRaises(ValueError):
            with ExceptionSilencer(Exception):
                int('aa')