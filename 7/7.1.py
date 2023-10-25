class Employee:
    name = None
    salary = None

    def show_name(self):
        print(self.name)


empl = Employee()
empl.name = 'Mark'

empl.show_name()
