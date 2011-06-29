#!/usr/bin/python3.1

import socket
import struct
import threading
from collections import namedtuple

UDP_IP="192.168.1.149"
UDP_PORT=50001


output_fields = ("time", "left", "right", "arm", "wrist", "grip")
datagram_format = "=" + "f" * len(output_fields)
Output = namedtuple("Output", output_fields)

output_values = {"time"  :    0.0,
                 "left"  :  110.0,
                 "right" :  110.0,
                 "arm"   : -700.0,
                 "wrist" :  200.0,
                 "grip"  :    2.0}

out_tuple = Output(**output_values)

class SendOutput(threading.Thread):
    def run(self):
        global out_tuple
        while True:
            message = struct.pack(datagram_format, *out_tuple)
            sock = socket.socket( socket.AF_INET, # Internet
                                  socket.SOCK_DGRAM ) # UDP
            sock.sendto( message, (UDP_IP, UDP_PORT) )
            out_tuple = out_tuple._replace(time = out_tuple.time+1)
            #print("message: ", message)

s = SendOutput()
s.daemon = True
s.start()
