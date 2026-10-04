class Employee:
    def calculate_salary(self):
        print("Employee salary")


class Manager(Employee):
    def calculate_salary(self):
        print("Manager salary: 50000")


class Developer(Employee):
    def calculate_salary(self):
        print("Developer salary: 40000")


Manager().calculate_salary()
Developer().calculate_salary()