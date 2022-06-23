#the input will be the number of steps and a string of down and up steps 
#and the number of vallies is required as a result
#there is a sea level and there are steps that go up and there are steps that go down 
# a valley is a sequence of steps that start from the sea level (0) and end at the sea level (0)
#which means that for counting the valleys we should count the number of sequences that 
#arch below the sea level.
from problems.solutions.counting_valleys import counting_valleys
import unittest


class TestCountingValleys(unittest.TestCase):
    def test_counting_valleys(self):
        self.assertEqual(counting_valleys(8, 'DDUUUUDD'),1)
        self.assertEqual(counting_valleys(5, 'DDUUU'),1)
        self.assertEqual(counting_valleys(5, 'DDUUD'),2)
        self.assertEqual(counting_valleys(42, 'DDDUDUUUUUUDDUUUDDDDDDDDDDUUUDDDDDUUUUUUUU'),2)
