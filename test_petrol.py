# There is a quota for every month for 60 liters of petrol
# you can buy as much petrol you want but only the amount of quota will be calculated 1500 Oshloobs the rest
# will be calculated as 3000 Oshloobs.
# Each month's quota will be transferred to the next month if not used.
# The input will contain a variable for the predicted amount of petrol that will be used next month. and a variable
# for the amount of quota left for this month to transfer to the next.
#
# The solution will be to first calculate the total quota for next month (left + 60) and then to subtract that
# from the predicted amount of petrol that will be used. If the result is less than 0, then first the total quota value
# will be multiplied to 1500 and added to the total sum, then the remained amount will be multiplied to -1 and then
# multiplied to 3000 and added to sum. If It's more than 0 the predicted amount will be multiplied to 1500 and returned
# if it's 0 the same will happen.

import unittest
from petrol import calculate_next_month_fuel_payment

class TestPetrol(unittest.TestCase):
    def test_calculate_next_month_fuel_payment_1(self):
        self.assertEqual(calculate_next_month_fuel_payment(41, 0), 61500)

    def test_calculate_next_month_fuel_payment_2(self):
        self.assertEqual(calculate_next_month_fuel_payment(125, 40), 225000)
