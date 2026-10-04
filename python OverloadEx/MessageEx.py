class Message:

    def welcome(self, name=None):
        if name is None:
            print("Welcome!")
        else:
            print("Welcome", name)


obj = Message()

obj.welcome()
obj.welcome("Ramya")