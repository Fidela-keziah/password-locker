import unittest
from user import User

class TestUser(unittest.TestCase):

    """
    Test class that defines test cases for the user class behaviours
    """

    def setUp(self):
        """
        use set up method
        """
        self.new_user = User("FidelaKeziah","fid@7")

    def test_init(self):

        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,"FidelaKeziah")
        self.assertEqual(self.new_user.password,"fid@7")

    def test_save_user(self):
        """
        test save user to test if the user is saved
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)


if __name__ == '__main__':
    unittest.main()
