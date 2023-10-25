class Employee:

    def setAge(self, age):
        self.age = age

    def getAge(self):
        print(self.age)


class Student(Employee):
    def setAge(self, age):
        if 18 < age < 65:
            self.age = age
        else:
            raise Exception("Not student")


student = Student()

student.setAge(32)
student.getAge()

student.setAge(100)
student.getAge()