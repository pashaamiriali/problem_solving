# there is a timeline from 1700 to 2700 in which the day of the programmer
# (the 256th day of the year) should be calculated. all teh properties of the
# timeline will be the same except the leap years will change in 1919 and before
# that each year will be determined by dividing the year to 4 and after that the
# leap year will be determined by checking if the year is divisible by 400 or is
# divisible by 4 and not 100. if the year is a leap year the month February will
# be 29 days long as for the normal years it will be 28 days long.
# on the year 1918 there is a break in the sequence of the days where the
# 32nd day of the year is feb 14th. which means that in the day of the programmer
# is on 26.9.1918 .
# from 1700 till 1917(inclusive) each year will be divided in 4 and if it is a
# normal year the day of the programmer will be calculated using a list of the months
# and their day counts. the program will loop through the list and sub the day of each
# month from the number of the programmers day (256) until the days lef are lower than
# the days of the current month. that will be the day of the month and the current month
# the month of the year and the year will be the given year. there will be two lists of
# months one for normal and one for leap years and the one for the leap years will have
# 29 as the number in its 1st element.

from problems.solutions.day_of_the_programmer import calculate_day_of_programmers, is_leap_year
import unittest


class TestDayOfProgrammer(unittest.TestCase):
    case_00 = (1918, '26.09.1918')
    case_01 = (1863, '13.09.1863')
    case_02 = (1984, '12.09.1984')
    case_03 = (2017, '13.09.2017')
    case_04 = (2016, '12.09.2016')
    case_05 = (1800, '12.09.1800')

    def test_day_of_programmer_case_00(self):
        self.assertEqual(calculate_day_of_programmers(
            self.case_00[0]), self.case_00[1])

    def test_day_of_programmer_case_01(self):
        self.assertEqual(calculate_day_of_programmers(
            self.case_01[0]), self.case_01[1])

    def test_day_of_programmer_case_02(self):
        self.assertEqual(calculate_day_of_programmers(
            self.case_02[0]), self.case_02[1])

    def test_day_of_programmer_case_03(self):
        self.assertEqual(calculate_day_of_programmers(
            self.case_03[0]), self.case_03[1])

    def test_day_of_programmer_case_04(self):
        self.assertEqual(calculate_day_of_programmers(
            self.case_04[0]), self.case_04[1])

    def test_day_of_programmer_case_05(self):
        self.assertEqual(calculate_day_of_programmers(
            self.case_05[0]), self.case_05[1])

    def test_is_leap_year(self):
        self.assertEqual(is_leap_year(2017),False)
        self.assertEqual(is_leap_year(2016),True)

# what did I learn?
# always pay attention to the exact outputs. when testing if possible copy the 
# provided expected outputs and paste them in your expected output. 
# beside testing your macro functions test your micro functions too. in 
# fact outline your code by writing tests for the micro and macro functions 
# that you are about to write so that you will have informative test failures.