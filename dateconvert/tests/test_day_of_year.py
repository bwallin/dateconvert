import unittest
from dateconvert import day_of_year
import datetime as dt


class TestDayOfYear(unittest.TestCase):

    def setUp(self):
        self.yyyymmdd = '20110101'
        self.yyyymmdd_dt = dt.datetime(2011, 01, 01)

    def test_result_is_datetime(self):

        actual = day_of_year.convert_to_datetime(self.yyyymmdd)
        expected = True

        self.assertEqual(expected, isinstance(actual, dt.datetime))


    def test_datetime_is_correct(self):

        actual = day_of_year.convert_to_datetime(self.yyyymmdd)
        expected = self.yyyymmdd_dt

        self.assertEqual(expected, actual)


    def test_result_is_correct(self):

        actual = day_of_year.calculate_day_of_year(self.yyyymmdd_dt)
        expected = '001'

        self.assertEqual(expected, actual)
