class Payment:
    def pay(self):
        print("Payment")


class CreditCardPayment(Payment):
    def pay(self):
        print("Paid using Credit Card")


class UPIPayment(Payment):
    def pay(self):
        print("Paid using UPI")


class CashPayment(Payment):
    def pay(self):
        print("Paid using Cash")


CreditCardPayment().pay()
UPIPayment().pay()
CashPayment().pay()