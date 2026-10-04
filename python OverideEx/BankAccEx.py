class BankAccount:
    def withdraw(self):
        print("Withdraw from bank account")


class SavingsAccount(BankAccount):
    def withdraw(self):
        print("Withdraw from savings account")


SavingsAccount().withdraw()