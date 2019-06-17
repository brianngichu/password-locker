import unittest
import pyperclip 
from credentials import Credentials
from user import User

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Argumentss:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''


    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("brian","ngichu","brianngichu@gmail.com","0706831353",'0000') 

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"brian")
        self.assertEqual(self.new_user.last_name,"ngichu")
        self.assertEqual(self.new_user.email,"brianngichu@gmail.com")
        self.assertEqual(self.new_user.phone_number,"0706831353")
        self.assertEqual(self.new_user.password,"0000")
    

    def test_save_multiple_user(self):
        '''
        test_save_multiple_contact to check if we can save multiple user
        objects to our contact_list 
        '''
        self.new_user.save_user() #saves the new user
        test_user = User("brian","ngichu","brianngichu@gmail.com","0706831353",'0000') # new user
        test_user.save_user()
        # test_user.save_contact()
        self.assertEqual(len(User.user_list),2)
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []
    

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("brian","ngichu","brianngichu@gmail.com","0706831353",'000') # new user
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)
    
    def test_find_user_by_number(self):
        '''
        test to check if we can find a user by phone number and display information
        '''

        self.new_user.save_user()
        test_user = User("brian","ngichu","brianngichu@gmail.com","0706831353",'0000') # new user
        test_user.save_user()

        found_user = User.find_by_number("0706831353")

        self.assertEqual(found_user.email,test_user.email)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("brian","ngichu","brianngichu@gmail.com","0706831353",'0000') # new user
        test_user.save_user()

        user_exists = User.user_exist("0706831353")

        self.assertTrue(user_exists)
    

    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(),User.user_list)
    

    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found user
        '''

        self.new_user.save_user()
        User.copy_email("brianngichu@gmail.com")

        self.assertEqual(self.new_user.email,pyperclip.paste())

if __name__ == '__main__':
    unittest.main()