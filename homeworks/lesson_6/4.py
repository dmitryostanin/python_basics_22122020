class Car:
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self, target_speed):
        self.speed = target_speed
        print(f'{self.name} is going')

    def stop(self):
        print(f'{self.name} has stopped')

    def turn(self, direction):
        print(f'{self.name} has turned {direction}')

    def show_speed(self):
        print(f'{self.name} speed is {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} speed is {self.speed} and it is exceeding speed limit (60)')
        else:
            print(f'{self.name} speed is {self.speed} ')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} speed is {self.speed} and it is exceeding speed limit (40)')
        else:
            print(f'{self.name} speed is {self.speed} ')


class PoliceCar(Car):
    pass


c1 = TownCar('Bus', 'Gray', 0, False)
c1.go(50)
c1.show_speed()
c1.turn('left')
c1.go(70)
c1.show_speed()
c1.stop()

c2 = SportCar('Lambo', 'Yellow', 0, False)
c2.go(200)
c2.show_speed()
c2.stop()

c3 = WorkCar('Garbage truck', 'Black', 0, False)
c3.go(50)
c3.show_speed()
c3.stop()

c4 = PoliceCar('Impala', 'White', 0, True)
c4.go(90)
c4.turn('right')
c4.show_speed()
c4.stop()
