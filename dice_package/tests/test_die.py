import unittest
from dice_package.dice import DiceBag, Die

class TestDie(unittest.TestCase):

    def setUp(self):
        self.dice_bag = DiceBag([6, 4, 8, 2])

    def test_upper(self):
        self.assertEqual(len(self.dice_bag.roll_bag()), 4)
