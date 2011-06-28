import socket
import struct

UDP_IP="127.0.0.1"
UDP_PORT=50001

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)

DATAGRAM_FORMAT = "@ffffff"

time = 0.0

while True:
    left  = 100.0
    right = 100.0
    arm   =   5.0
    wrist =   2.0
    grip  =   3.0
    
    message = struct.pack(DATAGRAM_FORMAT,
                          time,
                          left,
                          right,
                          arm,
                          wrist,
                          grip)
    
    #print("message:", message)
    
    sock = socket.socket( socket.AF_INET, # Internet
                          socket.SOCK_DGRAM ) # UDP
    sock.sendto( message, (UDP_IP, UDP_PORT) )
    time += 1
    
