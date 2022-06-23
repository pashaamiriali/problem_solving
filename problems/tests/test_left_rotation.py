# Given the array a and the positive integer d, do d left rotation operations on the arrray.
# one left rotation is the operation of taking the last element in the array and putting it in the 
# first index. 
# To do left rotations, first the first d elements of the array should be stored somewhere (support_a) so that
# they wouldn't get lost. then a loop will replace all of a[current_index - d] with a[current_index] 
# starting with a[d]. then another loop will replace the end of the array a[len(a) - d] till a[len(a)] with 
# the support_a. 
# I really should stop using languages without knowing the basic syntax :|
import unittest
from problems.solutions.left_rotation import rot_left


class TestLeftRotation (unittest.TestCase):
    def test_rot_left(self):
        self.assertEqual(rot_left([1, 2, 3, 4, 5, 6], 2), [3, 4, 5,6, 1, 2])
