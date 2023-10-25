class Employee:
    def __init__(self, name, age: int, salary: int):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def out(self):
        print(self.__name)
        print(self.__age)
        print(self.__salary)

empl = Employee('Mark',19,199999)
empl.out()