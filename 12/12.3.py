class Employee:
    def __init__(self, name, salary: int):
        self.name = name
        self.salary = salary

    def show(self):
        print(self.salary)

employee = Employee('Mark', 10004)
employee.show()