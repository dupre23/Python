from Ssh.SshClass import SshClass
from UserOptions.UserOptions2 import UserOptions

while True:
    UserOptions().listOptions()
    user_option=UserOptions().getUserOption()
    if user_option == '9':
        print("Goodbye!")
        break
    else:
        SshClass(host="127.0.0.1", user="user1", passwd="pass", port=2222).perform_action(user_option)