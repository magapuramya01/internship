student={
    "name":"Ramya",
    "course":"ccn",
    "age":17
}
try:
    key=int(input("Enter key value:"))
    print(student[key])
except KeyError:
    print("key is does not exist")