#!/usr/bin/python3.1

try:
    import wpilib
except:
    import fake_wpilib as wpilib

v = wpilib.Victor(1)
w = wpilib.Victor(2)
    
while True:
    v.set(0.7)
    w.set(0.5)
