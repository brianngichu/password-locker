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


    