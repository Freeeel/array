class User:
    _name = None
    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name


class Employee(User):
    def incName(self):
        if (len(self._name) > 0):
            self._name = self._name


empl = Employee()

empl.setName('Anatoly')

print(empl.getName())
