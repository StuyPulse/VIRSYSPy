#!/usr/bin/python3.1

try:
    import wpilib
except:
    import fake_wpilib as wpilib

v = wpilib.Jaguar(1)
w = wpilib.Jaguar(2)
    
while True:
    v.Set(1)
    w.Set(0.6)
