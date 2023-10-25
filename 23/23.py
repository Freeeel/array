class Position:
    name = None

    def __init__(self, name):
        self.name = name


class Department:
    name = None

    def __init__(self, name):
        self.name = name


class User:
    name = None
    position = None
    department = None

    def __init__(self, name, position, department):
        self.name = name
        self.position = position
        self.department = department


position = Position('Shofer')
department = Department('PMP')

user = User('Anatoly', position, department)

print(user.name)
print(user.position.name)
print(user.department.name)
