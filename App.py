from UserOptions.UserOptions import UserOptions
import subprocess

class DatabaseApp():

    def __init__(self):
        if not self.setup():
            print("Could not run setup. App will exit!")
            exit(1)
        self.main()
        exit(0)

    def resolveDependencies(self, install=False):
        c1 = ["pip", "show", "cx-oracle"]
        c2 = ["pip", "install", "cx-oracle"]
        try:
            out1 = subprocess.check_output(c1)
        except subprocess.CalledProcessError:
            print("Exception when running command: {}. Library is not installed.".format(' '.join(c1)))
            install = True
        if install:
            try:
                out2 = subprocess.check_output(c2)
            except subprocess.CalledProcessError:
                print("Exception when running command: {}".format(' '.join(c2)))
                return False
            if "Successfully installed cx-oracle" not in str(out2):
                print("Could not install dependencies!")
                return False
            print("Library was installed successfully!")
            return True
        else:
            if "Summary: Python interface to Oracle" in str(out1):
                print("Dependecies are already installed")
                return True

    def readCredentials(self):
        while True:
            username = input("Enter database username: ")
            password = input("Enter database password: ")
            if len(username) == 0:
                print ("No username was introduced!")
                continue
            elif len(password) == 0:
                print ("No password was introduced!")
                continue
            else:
                break
        return username, password

    def setup(self):
        if not self.resolveDependencies():
            print("Could not complete setup")
            return False
        self.username, self.password = self.readCredentials()
        return True

    def main(self):
        from Sql.SqlClass import SqlClass
        with SqlClass(self.username, self.password) as x:
            while True:
                UserOptions().listOptions()
                user_option = UserOptions().getUserOption()
                if user_option == '9':
                    print("Goodbye!")
                    break

if __name__ == '__main__':
    Run = DatabaseApp()