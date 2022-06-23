# there will be a 2d array which is 6by6 and the demand is to recognize all the 16
# hourglass patterns (shown below) in the array and then return the biggest sum found
# Figure 1 the hourglass pattern: a b c
#                                  d
#                                e f g
# the solution will be to first recognize the 3by3 arrays in the main array and then
# sum the hourglass in them and compare with the last mzx sum and then return the max.
# to recognize all the 3by3 arrays we should first set a limit of i&j-d(dimension 6) >=3
# when the limit for the inner loop is reached the loop will break and the same will
# happen for the outerloop on limit. as long as the limit is not reached the array will
# be allwed to be passed to the summing function.
import unittest
from problems.solutions.hourglass_sum import hourglass_sum


class TestHourglassSum (unittest.TestCase):
    def test_hourglass_sum(self):
        self.assertEqual(hourglass_sum([
            [-9, -9, -9, 1, 1, 1],
            [0, -9, 0, 4, 3, 2],
            [-9, -9, -9, 1, 2, 3],
            [0, 0, 8, 6, 6, 0],
            [0, 0, 0, -2, 0, 0],
            [0, 0, 1, 2, 4, 0]
        ]), 28)
        self.assertEqual(hourglass_sum([
            [1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 2, 4, 4, 0],
            [0, 0, 0, 2, 0, 0],
            [0, 0, 1, 2, 4, 0]
        ]), 19)
        self.assertEqual(hourglass_sum([
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]), 0)
#The ting that I failed to understand in this problem (which lead me to fail the tests)
# was that I didn't consider that the sums might be below zero. meaning that the biggest
# sum of the hourglasses might be below zero. thus setting my initial value of total to 
# zero and then comparing the next sums against it became problematic because the biggest 
# sum was something below zero and when the code was comparing these sums to it, it 
# didn't set the value of the sum because the initial value was bigger than the biggest 
# sum. my quick fix solution was to set the initial value to a large negative integer but 
# the proper solution would be to set the initial value of the sum to the sum of the first
# hourglass which would have made me to calculate the first one separately.