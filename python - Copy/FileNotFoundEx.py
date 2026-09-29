try:
    file=open("test.txt","r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("file does not exist")
