from drivebase import BBADriveBase

drive_base = BBADriveBase()

def run_command(cmd: str):
    if cmd == 'f':
        drive_base.forward()
    elif cmd == 'b':
        drive_base.reverse()
    elif cmd == 'l':
        drive_base.left()
    elif cmd == 'r':
        drive_base.right()
    elif cmd == 'i':
        drive_base.init()

def run(program: str):
    for cmd in program:
        run_command(cmd)