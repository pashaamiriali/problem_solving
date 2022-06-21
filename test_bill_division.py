# we have list of bills for items that Anna and Brian have ate.
# and we have the index of the item that Anna refused to eat.
# and also we have the total amount that Anna has to pay declared by Brian.
# we need to figure out the difference between the amount that anna actually
# has to pay which is the sum of the items in the bill list except the item that
# anna has refused to eat, divided by two. if the difference was 0 then we will
# print bonAppetit but if the difference was more than 0 we will print the difference.
from bill_division import compare_actual_with_given_charge, evaluate_bill_division, find_actual_charge
import unittest


class TestBillDivision(unittest.TestCase):
    # 0bills/1k,2b,3output
    test_case_input00 = ([3, 10, 2, 9], 1, 12, 5,)
    test_case_input01 = ([3, 10, 2, 9], 1, 7, 'Bon Appetit',)

    def test_evaluate_bill_division_case00(self):
        self.assertEqual(evaluate_bill_division(
            self.test_case_input00[0],
            self.test_case_input00[1],
            self.test_case_input00[2]),
            self.test_case_input00[3],)

    def test_evaluate_bill_division_case01(self):
        self.assertEqual(evaluate_bill_division(
            self.test_case_input01[0],
            self.test_case_input01[1],
            self.test_case_input01[2]),
            self.test_case_input01[3],)

    def test_find_actual_charge(self):
        self.assertEqual(find_actual_charge(
            self.test_case_input00[0],
            self.test_case_input00[1],), 7)

    def test_compare_actual_with_given_charge(self):
        self.assertEqual(compare_actual_with_given_charge(7, 7), 'Bon Appetit')
        self.assertEqual(compare_actual_with_given_charge(7, self.test_case_input00[2]),
                         self.test_case_input00[3])

# what I've learned from this problem was that I shouldn't copy paste before learning
# how to use the input tools. and I need to learn how to do that.