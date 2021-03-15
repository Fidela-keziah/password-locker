#!/usr/bin/env python3.6
import pyperclip
import unittest
from credential import Credential

class TestCredential(unittest.TestCase):

    """
    Test class that defines test cases for the credential class behaviours
    """

    def setUp(self):
        """
        use set up method
        """
        self.new_credential = Credential("instagram","FidelaKeziah","fid@7")

    def test_init(self):

        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.accountName,"instagram")
        self.assertEqual(self.new_credential.username,"FidelaKeziah")
        self.assertEqual(self.new_credential.password,"fid@7")

    def test_save_credential(self):
        """
        test save credential to test if the user is saved
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        Credential.credential_list = []

    def test_save_multiple_credential(self):
        """
        To test if you can save multiple credential 
        """
        self.new_credential.save_credential()
        test_credential = Credential("gmail","irafidela","fid@7")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

    def test_delete_credential(self):
        """
        To test if you can delete credential on the list
        """
        self.new_credential.save_credential()
        test_credential = Credential("gmail","irafidela","fid@7") 
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def test_password_generate(self):
        """
        Test case to check a user if he\she be capable to geberate password
        """
        password_generate = self.new_credential.password_generate()
        self.assertEqual(len(password_generate),8)

    def test_find_credential_by_username(self):
        """
        test to check if we can find a credential by username and display information
        """
        

        self.new_credential.save_credential()
        test_credential = Credential("gmail","irafidela","fid@7") 
        test_credential.save_credential()

        found_credential = Credential.find_by_username("irafidela")

        self.assertEqual(found_credential.accountName,test_credential.accountName)

    def test_copy_password(self):
        """
        Test to confirm that we are copying the password from a found credential
        """
        self.new_credential.save_credential()
        Credential.copy_password("FidelaKeziah")

        self.assertEqual(self.new_credential.password,pyperclip.paste())
    
    def test_credential_exists(self):

        """
        test to check if we can return a Boolean  if we cannot find the contact
        """

        self.new_credential.save_credential()
        test_credential = Credential("gmail","irafidela","fid@7")
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("irafidela")
        self.assertTrue(credential_exists)

    def test_display_credentials(self):
        """
        methods that test the display all credntial saved by user
        """
        self.assertEqual(Credential.display_credentials(),Credential.credential_list)


if __name__ == '__main__':
    unittest.main()