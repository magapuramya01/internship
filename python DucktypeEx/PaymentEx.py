class OnlinePayment:
    def process_payment(self):
        print("Online payment processed")


class CardPayment:
    def process_payment(self):
        print("Card payment processed")


class CashPayment:
    def process_payment(self):
        print("Cash payment processed")


def pay(obj):
    obj.process_payment()


pay(OnlinePayment())
pay(CardPayment())
pay(CashPayment())