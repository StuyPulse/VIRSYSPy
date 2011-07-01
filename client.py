#!/usr/bin/python3.1

import socket
import struct
import threading
from collections import namedtuple
from ctypes import *

UDP_OUT_IP="127.0.0.1"
UDP_OUT_PORT=50001
UDP_IN_PORT = 50002

OUTPUT_FIELDS = ("time",
                 "left",
                 "right",
                 "arm",
                 "wrist",
                 "grip")

INPUT_FIELDS = ("time",
                "left_angle",
                "right_angle",
                "arm_angle",
                "wrist_angle",
                "left_speed",
                "right_speed",
                "arm_speed",
                "wrist_speed",
                "heading_rate")

out_format_str = "=" + "f" * len(OUTPUT_FIELDS)
in_format_str = "=" + "f" * len(INPUT_FIELDS)

Output = namedtuple("Output", OUTPUT_FIELDS)
Input = namedtuple("Input", INPUT_FIELDS)

out_init_vals = dict([field, 0.0] for field in OUTPUT_FIELDS)
in_init_vals = dict([field, 0.0] for field in INPUT_FIELDS)

class SendOutput(threading.Thread):
    def __init__(self):
        self.out_tuple = Output(**out_init_vals)
        threading.Thread.__init__(self)

    def run(self):
        while True:
            message = struct.pack(out_format_str, *self.out_tuple)
            sock = socket.socket( socket.AF_INET, # Internet
                                  socket.SOCK_DGRAM ) # UDP
            sock.sendto( message, (UDP_OUT_IP, UDP_OUT_PORT) )
            self.update_output(time = self.out_tuple.time+1)
            #print("message: ", message)

    def update_output(self, **keywords):
        self.out_tuple = self.out_tuple._replace(**keywords)

class ReceiveInput(threading.Thread):
    def __init__(self):
        self.in_tuple = Input(**in_init_vals)
        threading.Thread.__init__(self)

    def is_newer(self, new_input):
        assert isinstance(new_input, Input)
        assert isinstance(self.in_tuple, Input)
        return (new_input.time > self.in_tuple.time)

    def run(self):
        sock = socket.socket( socket.AF_INET, # Internet
                              socket.SOCK_DGRAM ) # UDP
        sock.bind( ("", UDP_IN_PORT) )  # empty string is Python's INADDR_ANY
        while True:
            # buffer size (in bytes) holds a float for each input
            message = sock.recv(len(INPUT_FIELDS) * sizeof(c_float))
            print("received message:", message)
            new_in_tuple = Input(*struct.unpack(in_format_str, message))
            if self.is_newer(new_in_tuple):
                self.in_tuple = new_in_tuple
                print(self.in_tuple)

s = SendOutput()
s.daemon = True
s.start()

r = ReceiveInput()
r.daemon = True
r.start()
