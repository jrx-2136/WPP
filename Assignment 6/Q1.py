class PasswordManager:
    def __init__(self):
        self.passwords = []

    def get_password(self):
        if self.passwords:
            return self.passwords[-1]
        return None

    def set_password(self, new_password):
        if new_password not in self.passwords:
            self.passwords.append(new_password)

    def is_correct(self, password):
        return password == self.get_password()


pwd_mgr = PasswordManager()
pwd_mgr.set_password("pass2")
print(pwd_mgr.get_password())  # Shows current password
print(pwd_mgr.is_correct("pass1"))  # True or False
pwd_mgr.set_password("pass2")