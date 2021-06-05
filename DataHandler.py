import json


class DataHandler:
    PATH = "users_data.json"

    def __init__(self):
        self.parsedData = self.read()

    def read(self):
        with open(self.PATH) as file:
            return json.load(file)

    def updateDB(self):
        with open(self.PATH, "w") as file:
            json.dump(self.parsedData, file, indent=4)

    def setUserDetail(self, account_id, detail, new_value):
        if self.isAccountIDExists(account_id):
            if detail == "balance" and type(new_value) != int:
                return "The balance must be an number"
            self.parsedData[account_id][detail] = new_value
        return "Account ID doesn't exist."

    def getUserDetail(self, account_id, detail):
        if self.isAccountIDExists(account_id):
            return self.parsedData[account_id][detail]
        return "Account ID doesn't exist."

    def isAccountIDExists(self, account_id):
        if account_id in self.parsedData:
            return True
        return False
