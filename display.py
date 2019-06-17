import pyperclip
from user import User

#To add an account
def create_contact(email,phone,first_name,last_name,password):
    '''
    Function to create a new account
    '''
    new_user = User(email,phone,first_name,last_name,password)
    return new_user

#To save a user
def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()    
