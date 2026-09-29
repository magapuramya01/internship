try:
    age=int(input("enter age:"))
    if age<18:
        raise ValueError("age must be 18 years or above")
except ValueError as Error:
    print("Error:",Error)
else:
    print("You are eligibles")
