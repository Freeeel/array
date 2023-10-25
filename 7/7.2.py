class Employee:
    name = None
    salary = None

    def show_salary(self):
        print(self.salary)


empl = Employee()
empl.salary = 100000

empl.show_salary()
