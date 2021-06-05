from DataHandler import DataHandler

class ATMManager:
    def __init__(self):
        self.data = DataHandler()

    def get_user_detail(self, account_id, detail):
        return self.data.getUserDetail(account_id, detail)

    def get_balance(self, account_id):
        if self.data.isAccountIDExists(account_id):
            return self.data.getUserDetail(account_id, "balance")

    def cash_withdrawal(self, account_id, cash_withdrawal_amount):
        new_balance = self.get_balance(account_id) - int(cash_withdrawal_amount)
        self.data.setUserDetail(account_id, "balance", new_balance)
        return new_balance

    def cash_deposit(self, account_id, cash_deposit_amount):
        new_balance = self.get_balance(account_id) + int(cash_deposit_amount)
        self.data.setUserDetail(account_id, "balance", new_balance)
        return new_balance

    def save(self):
        self.data.updateDB()
