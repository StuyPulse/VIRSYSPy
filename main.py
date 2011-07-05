#!/usr/bin/python3.1

try:
    import wpilib
except:
    import fake_wpilib as wpilib

v = wpilib.Jaguar(1)
w = wpilib.Jaguar(2)
arm_motor = wpilib.Jaguar(3)
arm_gyro = wpilib.Gyro(1)

while True:
    v.Set(1)
    w.Set(0.6)
    arm_motor.Set(-1)
    print(arm_gyro.GetAngle())
