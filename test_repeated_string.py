#A string will be given to repeat and a number will be given to take a substring from that 
# repeated string based on it. then in that substring the number of the letter 'a' will be 
# counted and returned. 
# the substring should be taken from a string that is as large or larger than the number of 
# characters in that substring. so based on the length of the given string it will be 
# multiplied enough times so that it is larger than the length of the substring. then 
# the substring will be taken from it and the number of 'a's will be counted.
import unittest

from repeated_string import repeated_string

class TestRepeatedString(unittest.TestCase):
    def test_repeated_string(self):
        self.assertEqual(repeated_string('abcac',10),4)
        self.assertEqual(repeated_string('aba',10),7)
        self.assertEqual(repeated_string('a', 1000000000000), 1000000000000)
        self.assertEqual(repeated_string('gdadeadcaadaa', 12032), 5552)
        self.assertEqual(repeated_string('ceebbcb', 817723), 0)

        