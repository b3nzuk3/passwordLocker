import unittest
import os.path
from password import PasswordGenerator
from os import path

class TestUser_name(unittest.TestCase):

    def setUp(self):
        self.pm = PasswordGenerator("mykey")

    def test_create_pass(self):
        self.pm.create_pass()
        self.assertTrue(path.exists("accounts.txt"))


if __name__ == '__main__':
    unittest.main()
