import time


class TrafficLight:
    __color = None
    __color_periods = {
        'red': 7,
        'yellow': 2,
        'green': 6
    }

    def running(self, period=60):
        time_counter = 0
        while time_counter < period:
            for color, timing in self.__color_periods.items():
                self.__color = color
                print(self.__color)
                time.sleep(timing)
                time_counter += timing


tl = TrafficLight()
tl.running(90)
