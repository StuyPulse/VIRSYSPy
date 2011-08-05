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
        #while 1:
        #    print(self.arm_gyro.GetAngle())
        #    wpilib.Timer.Wait(0.05)
        
        #self.arm_motor.Set(-1)

        p = wpilib.PIDController(15, 1, 0, self.arm_gyro, self.arm_motor, 0.5)
        p.SetInputRange(-3.14, 3.14)
        p.SetOutputRange(-1, 1)
        p.SetSetpoint(0)
        p.Enable()

def run():
    robot = MyRobot()
    robot.StartCompetition()

if __name__ == "__main__":
    run()
