import unittest
from parsing import get_dates, first_run


class TestParsing(unittest.TestCase):

    def test_getdata(self):
        self.assertTrue(get_dates())

    def test_first(self):
        self.assertFalse(first_run())