from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port

class Sensors:
    distance_sensor = UltrasonicSensor(Port.S1)

    def should_turn(self) -> bool:
        return self.distance_sensor.distance() < 100