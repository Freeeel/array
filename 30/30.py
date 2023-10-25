class User:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def get_full_name(self):
        return (f"{self.name} {self.surname}")

    def get_sal(self):
        return self.salary


class Employee(User):
    def set_salary(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_sur(self, sur):
        self.sur = sur

    def get_sur(self):
        return self.sur


empl = Employee('Anatoly', 'Ivanov', 122200)
print('ДО\n')
print(empl.get_full_name())
print(empl.get_sal())
print('')

empl.set_salary(36000)
empl.set_name('Tom')
empl.set_sur('Antonovich')

print('ПОСЛЕ\n')
print(empl.get_name())
print(empl.get_sur())
print(empl.get_salary())