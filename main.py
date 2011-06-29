#!/usr/bin/python3.1

import client

#print("hello")
while True:
    #client.s.update_output(grip=4.0)
    client.s.update_output(**{"time"  :    0.0,
                              "left"  :  110.0,
                              "right" :  110.0,
                              "arm"   : -700.0,
                              "wrist" :  200.0,
                              "grip"  :    3.0})
