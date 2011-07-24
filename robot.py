#!/usr/bin/python3.1

try:
    import wpilib
except:
    import fake_wpilib as wpilib

class MyRobot(wpilib.SimpleRobot):
    def __init__(self):
        self.v = wpilib.Jaguar(1)
        self.w = wpilib.Jaguar(2)
        self.arm_motor = wpilib.Jaguar(3)
        self.arm_gyro = wpilib.Gyro(1)
        self.left_enc = wpilib.Encoder(6, 5)
        self.right_enc = wpilib.Encoder(8, 7)

    def Autonomous(self):
        p = wpilib.PIDController(0, 0, 0, self.arm_gyro, self.arm_motor)

        while self.IsAutonomous() and self.IsEnabled():
            self.v.Set(1)
            self.w.Set(1)
            #self.arm_motor.Set(-1)
            wpilib.Timer.Wait(1)
            self.v.Set(-1)
            self.w.Set(-1)
            #self.arm_motor.Set(-0.3)
            wpilib.Timer.Wait(1)

def run():
    robot = MyRobot()
    robot.StartCompetition()

if __name__ == "__main__":
    run()
