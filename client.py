#!/usr/bin/python3.1

import socket
import struct
import threading


UDP_IP="192.168.1.149"
UDP_PORT=50001
DATAGRAM_FORMAT = "=ffffff"

time = 0.0

class SendOutput(threading.Thread):
    def run(self):
        global time

        while True:
            left  =   110.0
            right =   110.0
            arm   =  -700.0
            wrist =   200.0
            grip  =     2.0
            
            message = struct.pack(DATAGRAM_FORMAT,
                                  time,
                                  left,
                                  right,
                                  arm,
                                  wrist,
                                  grip)
            
            sock = socket.socket( socket.AF_INET, # Internet
                                  socket.SOCK_DGRAM ) # UDP
            sock.sendto( message, (UDP_IP, UDP_PORT) )
            time += 1
            #print("message: ", message)

s = SendOutput()
s.daemon = True
s.start()
