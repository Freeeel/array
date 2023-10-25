class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(self.name)

employee = Employee('Mark', '1000000')
employee.show()