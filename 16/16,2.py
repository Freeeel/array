class Employee:

    __name = None
    __age = None
    __salary = None

    def __init__(self, name, age:int, salary:int):
        self.__name = name
        self.__age = age
        self.__salary = salary

empl = Employee('Mark',19,100000)