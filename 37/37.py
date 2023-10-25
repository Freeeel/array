class User:
    def setName(self, name):
        if self._notEmpty(name):
            self.name = name

    def getName(self):
        return self._notEmpty(self.name)

    def _notEmpty(self, stri):
        return len(stri) > 0


class Employee(User):
    def setSurn(self, surname):
        if self._notEmpty(surname):
            self.surname = surname

    def getSurn(self):
        return self._notEmpty(self.surname)


empl = Employee()

empl.setName('Anatoly')
empl.setSurn('Ivanov')

print(empl.getName())
print((empl.getSurn()))
