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

init_vals = dict([field, 0.0] for field in output_fields)

class SendOutput(threading.Thread):
    def __init__(self):
        self.out_tuple = Output(**init_vals)
        threading.Thread.__init__(self)

    def run(self):
        while True:
            message = struct.pack(datagram_format, *self.out_tuple)
            sock = socket.socket( socket.AF_INET, # Internet
                                  socket.SOCK_DGRAM ) # UDP
            sock.sendto( message, (UDP_IP, UDP_PORT) )
            self.update_output(time = self.out_tuple.time+1)
            #print("message: ", message)

    def update_output(self, **keywords):
        self.out_tuple = self.out_tuple._replace(**keywords)


s = SendOutput()
s.daemon = True
s.start()
