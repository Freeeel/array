class Employee:
    __name = None
    __salary = None

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def getName(self):
        return self.__name
    def getSalary(self):
        return self.__salary


users = [
    Employee('Kostya', 10000),
    Employee('Andrei', 20000),
    Employee('Vasya', 304000),
]

for user in users:
    print(user.getName(), user.getSalary())