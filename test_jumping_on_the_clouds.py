# input is an array of clouds and output will be the fastest path to finish the game
# the clouds with the number 1 on them are to be avoided and the player can either
# move one cloud ahead or two
#so, the priority with the steps is the furthest which is 2 steps and if a 2 step 
# move ended up in a thunderhead cloud, the loop will go one step ahead
import unittest

from jumping_on_the_clouds import jumping_on_clouds
class TestJumpingOnTheColoud(unittest.TestCase):
    def test_jumping_on_the_clouds(self):
        self.assertEqual( jumping_on_clouds([0,1,0,0,0,1,0]),3)