   
balance=5000
try:
    amount=float(input("enter withdraw amount"))
    if amount<=0:
       raise ValueError("the withdraw amount must be greaterthan zero")
    if amount >  balance:
        raise ValueError("insufficient balance")
    balance = balance-amount
except ValueError as error:
       print("transaction failed",error)
else:
    print("withdrawal succesful")
    print("remaining balance",balance)
finally:
    print("thankyou!")