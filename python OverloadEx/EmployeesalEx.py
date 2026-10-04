class Employee:

    def salary(self, basic, bonus=0):
        return basic + bonus


obj = Employee()

print("Salary:", obj.salary(20000))
print("Salary with bonus:", obj.salary(20000, 5000))