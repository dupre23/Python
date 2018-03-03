import re

class UserOptions():
    options = {'1': 'Add user', '2': 'Delete user', '3': 'List users','9':'Exit'}

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

    def getDeleteUserFields(self):
        while True:
            delete_type = input("a-Delete by ID \nb-Delete by username\nEnter delete option: ")
            if delete_type != "a" and delete_type != "b":
                print("Invalid delete choice was introduced!")
                continue
            break
        while True:
            if delete_type == "a":
                delete_id = input("Delete ID: ")
                if not delete_id.isdigit():
                    print("ID should be a digit!")
                    continue
            if delete_type == "b":
                delete_username = input("Delete username: ")
                if len(delete_username) == 0:
                    print("Null username was introduced!")
                    continue
                if delete_username.isdigit():
                    print("Username should not contain digits only!")
                    continue
            break
        if delete_type == "a":
            return delete_type, delete_id
        else:
            return delete_type, delete_username