class Car:
    color = None
    fuel = None
    mark = None
    model = None
    v = None

    def go(self):
        print("Едем!")

    def turn(self):
        print("Поворот!")

    def stop(self):
        print("Стоп!")


myCar = Car()
myCar.color = 'red'
myCar.fuel = 50
myCar.mark = 'Nissan'
myCar.model = 'Skyline x'
myCar.v = '3.7'

myCar.go()
myCar.turn()
myCar.stop()