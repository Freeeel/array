class Employee:
    def run(self, name, salary):
        return name + ' ' + salary


empl = Employee()

print(empl.run('Mark', '100000'))
