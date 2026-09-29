try:
    number1=int(input("enter first number:"))
    number2=int(input("enter second number:"))
    result=number1/number2
except ValueError:
    print("enter numbers")
except ZeroDisivionError:
    print("this is a zero division error")
else:
    print("result",result)
finally:
    print("ths progrm is succesfully completed")