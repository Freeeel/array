class Employee:
    __name = None

    def __init__(self, name, surname):
        self.__name = name


emp1 = Employee('john')
emp2 = Employee('eric')

print(emp1 == emp1)
#True