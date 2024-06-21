#Draven McConathy
#06/21/2024

import unittest
from Share import *

class ShareTestCase(unittest.TestCase):
    def setUp(self):
        self.share = Share(0, "Savings", .05, 25)

    def test_get_interestRate(self):
        self.assertEqual(self.share.get_interestRate(), .05)

    def test_get_currentBalance(self):
        self.assertEqual(self.share.get_currentBalance(), 0)

    def test_get_shareName(self):
        self.assertEqual(self.share.get_shareName(), "Savings")

    def test_change_interestRate(self):
        self.assertEqual(self.share.get_interestRate(), .05)
        self.share.change_interestRate(.10)
        self.assertEqual(self.share.get_interestRate(), .10)

    def test_deposit_funds(self):
        self.assertEqual(self.share.get_currentBalance(), 0)
        self.share.deposit_funds(50)
        self.assertEqual(self.share.get_currentBalance(), 50)

    def test_withdraw_funds(self):
        self.share.deposit_funds(50)

        #Tests to make sure money can be withdrawn
        self.assertEqual(self.share.get_currentBalance(), 50)
        self.share.withdraw_funds(20)
        self.assertEqual(self.share.get_currentBalance(), 30)

        #Tests to make sure money can not be withdrawn beyond minimumBalance
        self.share.withdraw_funds(20)
        self.assertEqual(self.share.get_currentBalance(), 30)

if __name__ == '__main__':
    unittest.main()