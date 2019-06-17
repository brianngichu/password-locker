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
        test_user = User("brianngichu@gmail.com","0706831353","NgongRoad","NgongLane",'0000') # new user
        test_user.save_user()
        # test_user.save_contact()
        self.assertEqual(len(User.user_list),2)

if __name__ == '__main__':
    unittest.main()