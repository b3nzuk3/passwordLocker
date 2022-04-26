import unittest
import os.path
from os import path
from username import User_name

class TestUser_name(unittest.TestCase):


    def setUp(self):
        self.new_user = User_name()


    def test_init(self):
        self.assertNotEqual(self.new_user, None)


    def test_save_user(self):
        self.new_user.save_user("hussein")
        self.assertEqual(len(User_name.users),1)

    def test_save_account(self):
        site = "netflix"
        password = "1234"
        self.new_user.save_account(site, password)
        self.assertTrue(path.exists("accounts.txt"))

    def test_del_contact(self):
        path = "netflix"
        self.new_user.del_account(path)
        self.assertFalse(self.new_user.search_account("netflix"))

    def test_display_contact(self):
        self.new_user.display_contact()
        self.assertTrue(path.exists("accounts.txt"))

    def test_search_account(self):
        site = "netflix"
        self.new_user.search_account(site)
        self.assertTrue(self.new_user.search_account("netflix"))




if __name__ == '__main__':
    unittest.main()
