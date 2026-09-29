correct_username="admin"
correct_password="Ram1319"
try:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username!=correct_username:
        raise ValueError("invalid username")
    if password!=correct_password:
      raise ValueError("invalid password")
except ValueError as error:
    print("invalid login")
else:
    print("login successfully!")