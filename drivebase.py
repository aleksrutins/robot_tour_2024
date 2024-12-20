from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

GRID_SIZE = -500 # motors are mounted backwards


class BBADriveBase(DriveBase):

    def __init__(self):
        self.left_motor = Motor(Port.A)
        self.right_motor = Motor(Port.B)
        super().__init__(self.left_motor, self.right_motor, 55, 227.5)

    def init(self):
        self.straight(GRID_SIZE / 2)

    def forward(self):
        self.straight(GRID_SIZE)

    def reverse(self):
        self.straight(-GRID_SIZE)

    def left(self):
        self.turn(90) # motors backwards

    def right(self):
        self.turn(-90) # motors backwards
