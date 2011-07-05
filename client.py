#!/usr/bin/python3.1

import socket
import struct
import threading
from collections import namedtuple
from ctypes import *
import configparser

# Set up input/output structures
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

# Classes to hold input and output data
Output = namedtuple("Output", OUTPUT_FIELDS)
Input = namedtuple("Input", INPUT_FIELDS)

# Get network data from config file
net_cfg = configparser.ConfigParser()
net_cfg.read("network.conf")
UDP_OUT_IP   = net_cfg.get("Network", "VIRSYS_IP")
UDP_OUT_PORT = net_cfg.getint("Network", "VIRSYS_RECV_PORT")
UDP_IN_PORT  = net_cfg.getint("Network", "LOCAL_RECV_PORT")

# Read port numbers for robot I/O
# User configures port numbers to match sensors and actuators on the real robot
port_cfg = configparser.ConfigParser()
port_cfg.read("cRIO_ports.conf")
ports = {}
for section in port_cfg.sections():
    ports[section] = {}
    for port_name in port_cfg.options(section):
        ports[section][port_cfg.getint(section, port_name)] = port_name

class SendOutput(threading.Thread):
    """
    Sends output (motor torques) to VIRSYS's physics simulator.
    Stores the latest values set by the robot in an Output buffer, and
    continuously sends the values to VIRSYS in a separate thread.
    """

    def __init__(self):
        out_init_vals = dict([field, 0.0] for field in OUTPUT_FIELDS)
        self.out_tuple = Output(**out_init_vals)
        self.format_str = "=" + "f" * len(OUTPUT_FIELDS)
        threading.Thread.__init__(self)

    def run(self):
        """
        Continuously flush Output buffer to VIRSYS
        """
        while True:
            message = struct.pack(self.format_str, *self.out_tuple)
            sock = socket.socket( socket.AF_INET, # Internet
                                  socket.SOCK_DGRAM ) # UDP
            sock.sendto( message, (UDP_OUT_IP, UDP_OUT_PORT) )
            self._update_buffer(time = self.out_tuple.time+1)

    def _update_buffer(self, **keywords):
        """
        Store a new value or values in the Output buffer
        """
        self.out_tuple = self.out_tuple._replace(**keywords)

    def update_output(self, type_name, port, value):
        """
        Store a new output value to a given port number.
        """
        self._update_buffer(**{ports[type_name][port] : value})

class ReceiveInput(threading.Thread):
    """
    Receives input (sensor values) from VIRSYS and stores it in an
    Input buffer for access by sensor classes in robot code.
    """

    def __init__(self):
        in_init_vals = dict([field, 0.0] for field in INPUT_FIELDS)
        self.in_tuple = Input(**in_init_vals)
        self.format_str = "=" + "f" * len(INPUT_FIELDS)
        threading.Thread.__init__(self)

    def is_newer(self, new_input):
        """
        Check if the next datagram is more recent than the one in the buffer.
        UDP datagrams are unreliable and may come out of order, so we have to
        check the timestamp before accepting new data.
        """
        assert isinstance(new_input, Input)
        assert isinstance(self.in_tuple, Input)
        return (new_input.time > self.in_tuple.time)

    def get_value(self, type_name, port):
        return self.in_tuple._asdict()[ports[type_name][port]]

    def run(self):
        """
        Continuously receive input from VIRSYS and store it in an Input buffer
        """
        sock = socket.socket( socket.AF_INET, # Internet
                              socket.SOCK_DGRAM ) # UDP
        sock.bind( ("", UDP_IN_PORT) )  # empty string is Python's INADDR_ANY
        while True:
            # buffer size (in bytes) holds a float for each input
            message = sock.recv(len(INPUT_FIELDS) * sizeof(c_float))
            new_in_tuple = Input(*struct.unpack(self.format_str, message))
            if self.is_newer(new_in_tuple):
                self.in_tuple = new_in_tuple

s = SendOutput()
s.daemon = True
s.start()

r = ReceiveInput()
r.daemon = True
r.start()
