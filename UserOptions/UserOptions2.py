from Ssh.SshClass import SshClass

class UserOptions():
    options = {'1': 'Add user', '2': 'Delete user', '3': 'Verify user','9':'Exit'}

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