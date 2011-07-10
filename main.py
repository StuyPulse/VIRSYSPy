#!/usr/bin/python3.1

try:
    import wpilib
except:
    import fake_wpilib as wpilib

v = wpilib.Jaguar(1)
w = wpilib.Jaguar(2)
arm_motor = wpilib.Jaguar(3)
arm_gyro = wpilib.Gyro(1)
left_enc = wpilib.Encoder(6, 5)
right_enc = wpilib.Encoder(8, 7)

while True:
    v.Set(1)
    w.Set(1)
    #    arm_motor.Set(-1)
    wpilib.Timer.Wait(1)
    v.Set(-1)
    w.Set(-1)
    #    arm_motor.Set(-0.3)
    wpilib.Timer.Wait(1)
