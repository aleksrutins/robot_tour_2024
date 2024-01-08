from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from sensors import Sensors
from util import Vec2
from enum import Enum

class Direction(Enum):
    FORWARD = 0
    REVERSE = 1
    LEFT = 2
    RIGHT = 3

class Axis(Enum):
    X = 0
    Y = 1

GRID_SIZE = 500

class BBADriveBase(DriveBase):
    sensors = Sensors()

    def __init__(self):
        self.left_motor = Motor(Port.A)
        self.right_motor = Motor(Port.B)
        super().__init__(self.left_motor, self.right_motor, 55.5, 104)
    
    def run_grid(self, direction: int, distance: int):
        if direction == FORWARD:
            self.straight(distance * GRID_SIZE)
        elif direction == REVERSE:
            self.straight(-distance * GRID_SIZE)
        elif direction == LEFT:
            self.turn(-90)
            self.run_grid(FORWARD, distance)
            self.turn(90)
        elif direction == RIGHT:
            self.turn(90)
            self.run_grid(FORWARD, distance)
            self.turn(-90)
    
    def switch_axis(axis: int) -> int:
        if axis == X:
            return Y
        else:
            return X
    
    def axis_direction(axis: int, difference: int) -> int:
        if axis == X:
            if difference < 0:
                return LEFT
            else:
                return RIGHT
        else:
            if difference < 0:
                return REVERSE
        return FORWARD
    
    def run_to_target(self, start: Vec2, target: Vec2):
        current_pos = start

        axis = X

        while current_pos.x != target.x and current_pos.y != target.y:
            difference = Vec2.diff(target, current_pos)

            if current_pos.x == target.x and current_pos.y != target.y:
                axis = Y
            elif current_pos.x != target.x and current_pos.y == target.y:
                axis = X

            if self.sensors.should_turn():
                axis = self.switch_axis(axis)

            delta = 0
            if axis == X:
                delta = difference.x
            else:
                delta = difference.y

            self.run_grid(self.axis_direction(axis, delta), 1)