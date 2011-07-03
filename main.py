#!/usr/bin/python3.1

import client

while True:
    client.s.update_output("PWMOut", 1, 110)
    client.s.update_output("PWMOut", 2, 110)
    client.s.update_output("PWMOut", 3, -700)
    client.s.update_output("PWMOut", 4, 200)
    client.s.update_output("PWMOut", 5, 3)
    
