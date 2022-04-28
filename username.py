from password import PasswordGenerator


class User_name:

    users = []

    def __init__(self):
        """
        first we make instances of the variables
        """
        self.user_name = None
        self.pass_word = None

    def save_user(self,user):
        """
        this method allows the ability to save user in a list
        """


        User_name.users.append(user)

    def save_account(self, site, password):

        """
        allows user to save account credentials once created
        """
        with open("accounts.txt", "a+") as f:
            f.write("Website: " + site + " "+ " Password: " + password +"\n")

    def del_account(self,site):
        """
        method to facilitate deletion of credentials in the future
        """
        with open("accounts.txt", "r") as f:
            lines = f.readlines()
        with open("accounts.txt", "w") as f:
            for line in lines:
                if site not in line:

                    f.write(line)

        return line

    def display_contact(self):
        """
        method allows the displaying of user credentials saves in a file
        """

        with open("accounts.txt", "r") as f:
            lines = f.read()
            return lines

    def search_account(self,site):
        """
        allows user to such for specefic account and saves time
        """
        mylines = []
        with open("accounts.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                if site in line:
                    mylines.append(line)
            for element in mylines:
                return element
