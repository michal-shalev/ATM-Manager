from DataHandler import DataHandler


class UserAuthentication:
    def __init__(self):
        self.data = DataHandler()

    def authentication(self, account_id, password):
        if self.isAccountIDExists(account_id):
            user_password = self.data.getUserDetail(account_id, "password")
            if user_password == password:
                return True
        return False

    def isAccountIDExists(self, account_id):
        return self.data.isAccountIDExists(account_id)