#there is a pile of socks that needs to be first grouped together in a way that the matching 
# socks are in one container together then the socks in each container should be counted and 
# the number of socks in it divided by two (if the number is odd one should be subtracted from it)
# then the number of pairs from each container should be added together and the total number of 
# matches should be returned.
import unittest
from problems.solutions.sales_by_match import sock_merchant
class TestSalesByMatch(unittest.TestCase):
    def test_sock_merchant_01(self):
        self.assertEqual(sock_merchant(7, [1, 2, 1, 2, 1, 3, 2]), 2)

    def test_sock_merchant_02(self):
        self.assertEqual(sock_merchant(12, [5,3,4,3,5,4,3,4,3,4,5,6]), 5)

    def test_sock_merchant_03(self):
        self.assertEqual(sock_merchant(8, [3,3,3,3,4,4,4,4]), 4)
