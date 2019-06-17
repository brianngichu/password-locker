import pyperclip
from user import User
from credentials import Credentials
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
#To delete user
def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()



def main():
    print("\033[1;36;40m PASSWORD LOCKER App\n")
    print("")
    done = input("Hello, welcome to Password Locker  what's your name? ")
    print("  ")
    print("hello, " + done + ", To get you started, kindly choose one of the following .")
    print(" ")
    print("\033[1;34;1m  Options On how to Get Started on Password Locker\n")
    print("")
  


    while True:

        list =('''
        1-Create new account
        2-Display accounts
        3-Search for accounts
        4-Exit Password-Locker
        ''')
        print(list)
        print("Use these short codes : 1 - create a new user, 2 - display users, 3 -find a user, 4 -exit the Password locker ")

        short_code = input().lower()

        if short_code == '1':
            print("New User")
            print("-"*10)

            print("Email Address ...")
            e_address = input()

            print("Phone Number ...")
            p_number = input()

            print ("First Name ....")
            f_name = input()

            print("Last Name ...")
            l_name = input()

            print("Password ...")
            password = input()

            print("Confirm Password ...")
            password1 = input()

            if password == password1:
                create_user = User(e_address,p_number,f_name,l_name,password)
                create_user.save_user() # create and save new user.
                print ('\n')
                print(f"New User {f_name} {l_name} created")
                print ('\n')

        elif short_code == '2':

            if display_users():
                print("Here is a list of all your users")
                print('\n')

                for user in display_users():
                    print(f"{user.first_name} {user.last_name} .....{user.phone_number}")

                    print('\n')
                else:
                    print('\n')

                    print('\n')

        elif short_code == '3':

            print("Enter the number you want to search for")

            search_number = input()
            if check_existing_user(search_number):
                search_user = find_user(search_number)
                print(f"{search_user.first_name} {search_user.last_name}")
                print('-' * 20)

                print(f"Phone number.......{search_user.phone_number}")
                print(f"Email address.......{search_user.email}")
            else:
                print("That user does not exist")

        elif short_code == "4":
            print("Thank you for using our services. Welcome again .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':
    main()