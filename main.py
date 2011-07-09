#!/usr/bin/python3.1

try:
    import wpilib
except:
    import fake_wpilib as wpilib

import time

v = wpilib.Jaguar(1)
w = wpilib.Jaguar(2)
arm_motor = wpilib.Jaguar(3)
arm_gyro = wpilib.Gyro(1)
left_enc = wpilib.Encoder(6, 5)
right_enc = wpilib.Encoder(8, 7)

print("ldist\tlrate\t\trdist\trrate")
while True:
    v.Set(0.4)
    w.Set(0.4)
    arm_motor.Set(-1)
    print("%f\t%f\t\t%f\t%f" %
          (left_enc.GetDistance(), left_enc.GetRate(),
           right_enc.GetDistance(), right_enc.GetRate()))
    time.sleep(0.05)
