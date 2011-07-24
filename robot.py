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
        p = wpilib.PIDController(0.5, 0.25, 0.1, self.arm_gyro, self.arm_motor)
        print(p.GetP(), p.GetI(), p.GetD())
        p.SetPID(1, 0.5, 0.25)
        print(p.GetP(), p.GetI(), p.GetD())
        wpilib.Timer.Wait(1)
        p.Enable()
        wpilib.Timer.Wait(1.5)
        p.Disable()

def run():
    robot = MyRobot()
    robot.StartCompetition()

if __name__ == "__main__":
    run()
