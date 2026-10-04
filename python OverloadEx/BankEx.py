class Bank:

    def deposit(self, amount, bonus=0):
        return amount + bonus


obj = Bank()

print("Deposit:", obj.deposit(5000))
print("Deposit:", obj.deposit(5000, 1000))