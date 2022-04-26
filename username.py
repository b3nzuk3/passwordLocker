from password import PasswordGenerator


class User_name:

    users = []

    def __init__(self):
        self.user_name = None
        self.pass_word = None

    def save_user(self,user):
        User_name.users.append(user)

    def save_account(self, site, password):
        with open("accounts.txt", "a+") as f:
            f.write("Website: " + site + " "+ " Password: " + password +"\n")

    def del_account(self,site):

        with open("accounts.txt", "r") as f:
            lines = f.readlines()
        with open("accounts.txt", "w") as f:
            for line in lines:
                if site not in line:

                    f.write(line)

        return line

    def display_contact(self):

        with open("accounts.txt", "r") as f:
            lines = f.read()
            return lines

    def search_account(self,site):
        mylines = []
        with open("accounts.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                if site in line:
                    mylines.append(line)
            for element in mylines:
                return element
