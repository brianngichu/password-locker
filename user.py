import pyperclip

class User:

    user_list = []  # Empty user list

    def __init__(self, email, number, first_name, last_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = number
        self.password = password

    contact_list = [] # Empty contact list
    # Init method up here

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

        # Init method up here

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)
    
    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a user that matches that number.
        Argumantss:
            number: Phone number to search for
        Returns :
            User of person that matches the number.
        '''

        for user in cls.user_list:
            if user.phone_number == number:
                return user
    
    @classmethod
    def user_exist(cls,number):
        '''
        Method that checks if a user exists from the user list.
        Argumantss:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.phone_number == number:
                return True
        return False
    
    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list
    
    @classmethod
    def display_user(cls):
        for user in cls.user_list:
            return user 
    
    @classmethod
    def copy_email(cls,number):
        user_found = User.find_by_number(number)
        pyperclip.copy(user_found.email)

    