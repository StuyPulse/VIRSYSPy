#!/usr/bin/python3.1

try:
    import wpilib
except:
    import fake_wpilib as wpilib

v = wpilib.Jaguar(1)
w = wpilib.Jaguar(2)
    
while True:
    v.set(1)
    w.set(0.6)
