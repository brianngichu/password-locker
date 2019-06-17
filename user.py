class User:

    user_list = []  # Empty user list

    def __init__(self, email, number, first_name, last_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = number
        self.password = password

    contact_list = [] # Empty contact list