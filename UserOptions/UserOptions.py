import re

class UserOptions():
    options = {'1': 'Add user', '9':'Exit'}

    def listOptions(self):
        for option, action in UserOptions.options.items():
            print(option + ' --- ' + action)

    def getUserOption(self):
        while True:
            self.user_option = input("Enter option: ")
            if len(self.user_option) != 1:
                print("Invalid option length!")
                continue
            elif self.user_option not in UserOptions.options.keys():
                print("Invalid option was indicated")
                continue
            else:
                break
        return self.user_option

    def getAddUserFields(self):
        email_pattern = r'\S+@\S+.[a-z]{2,3}'
        while True:
            first_name = input("First name: ")
            last_name = input("Last name: ")
            if (len(first_name) or len(last_name)) < 2:
                print("Invalid length for first_name/last_name")
                continue
            email = input("Email: ")
            if not re.match(email_pattern, email):
                print("Invalid email format")
                continue
            break
        username = first_name[0:2] + last_name
        return first_name, last_name, email, username