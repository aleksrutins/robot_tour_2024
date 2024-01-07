from pybricks.iodevices import Ev3devSensor
from pybricks.parameters import Port

class Sensors:
    distance_sensor = Ev3devSensor(Port.S1)

    def should_turn(self) -> bool:
        return self.distance_sensor.read('DC_ALL')[6] < 100