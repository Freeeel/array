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

    def info(self):
        print(f"Автомобиль {self.mark} {self.model}, с объемом двигателя {self.v}")
        print(f"Цвет автомобиля: {self.color}")
        print(f"Топлива в баке: {self.fuel}")


myCar = Car()
myCar.color = 'red'
myCar.fuel = 50
myCar.mark = 'Nissan'
myCar.model = 'Skyline x'
myCar.v = '3.7'

myCar.go()
myCar.turn()
myCar.stop()
myCar.info()
