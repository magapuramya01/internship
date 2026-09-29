try:
    number=int(input("enter a number:"))
    print(100/number)
except ZeroDivisionError:
    print("cannot divided by zero:")
finally:
    print("program completed")