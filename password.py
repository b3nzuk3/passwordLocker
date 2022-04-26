from cryptography.fernet import Fernet


class PasswordGenerator:

    def __init__(self, key):
        self.key = key


    def create_pass(self):
        self.key = Fernet.generate_key()
        with open("password.txt", 'wb') as f:
            f.write(self.key)


# pm = PasswordGenerator("mykey")
# print(pm.create_pass())
