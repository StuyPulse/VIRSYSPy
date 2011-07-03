#!/usr/bin/python3.1

import client
try:
    import wpilib
except:
    import fake_wpilib as wpilib

while True:
    client.s.update_output("PWMOut", 1, 110)
    client.s.update_output("PWMOut", 2, 110)
    client.s.update_output("PWMOut", 3, -700)
    client.s.update_output("PWMOut", 4, 200)
    client.s.update_output("PWMOut", 5, 3)
    
