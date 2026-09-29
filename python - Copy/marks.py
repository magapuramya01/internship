try:
    marks=float(input("enter marks:")) 
    if marks<0 or marks>100:
        raise ValueError("marks must be between 0 to 100 ")
except ValueError as error:
    print("invalid marks:",error)
else:
    if marks>=35:
        print("student passed")
    else:
        print("sorry you are fali")