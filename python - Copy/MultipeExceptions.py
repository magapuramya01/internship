try:
    a=int(input("Enter a first number:"))
    b=int(input("Enter a second number:"))
    print("result=",a/b)
except ValueError:
    print("enter integer values:")
except ZeroDivisionError:
    print("it is a zero division error:")

