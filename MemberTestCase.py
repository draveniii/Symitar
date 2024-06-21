#Draven McConathy
#06/19/2024


import unittest
from Member import *

class MemberTestCase(unittest.TestCase):
    def setUp(self):
        self.member = Member("Draven McConathy", "333 Street Name", "05/18/2001")

    def test_get_memberName(self):
        self.assertEqual(self.member.get_memberName(), "Draven McConathy")
        
    def test_get_MemberAddress(self):
        self.assertEqual(self.member.get_memberAddress(), "333 Street Name")

    def test_get_memberDOB(self):
        self.assertEqual(self.member.get_memberDOB(), "05/18/2001")

    def test_change_memberName(self):
        self.assertEqual(self.member.get_memberName(), "Draven McConathy")
        self.member.change_memberName("Mercedes Helliangao")
        self.assertEqual(self.member.get_memberName(), "Mercedes Helliangao")

    def test_change_memberAddress(self):
        self.assertEqual(self.member.get_memberAddress(), "333 Street Name")
        self.member.change_memberAddress("444 Road Name")
        self.assertEqual(self.member.get_memberAddress(), "444 Road Name")

if __name__ == '__main__':
    unittest.main()

