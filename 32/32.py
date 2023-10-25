class User:
    def setAge(self, age):
        if (age >= 0):
            self.age = age
        else:
            raise Exception('EROR')

    def getAge(self):
        return self.age


class Employee(User):
    def setAge(self, age):
        if (age <= 120):
            super().setAge(age)
        else:
            raise Exception('EROR')
