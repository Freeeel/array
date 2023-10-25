class Student:

    name = None
    surname = None

    def up(self, char):

        for i in range(len(char)):
            if i != 0:
                print(char[i], end='')
            else:
                print(char[i].upper(), end='')

student = Student()

student.name = 'mark'
student.surname = 'sina'
student.up(student.name)
student.up(student.surname)
