languages=["html","css","javascript","Bootstrap"]
print(languages)
try:
    index=int(input("Enter index value:"))
    print(languages[index])
except ValueError:
    print("enter an interger:")
except IndexError:
    print("index dosn not exist")