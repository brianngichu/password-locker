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
#To find user
def find_user(number):
    '''
    Function that finds a user by number and returns the user
    '''
    return User.find_by_number(number)    
#To check existing user
def check_existing_user(number):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return User.user_exist(number)
#To display users
def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()
