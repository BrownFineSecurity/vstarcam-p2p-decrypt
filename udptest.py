#!/usr/bin/env python3
import time
import socket
import sys

m1 = bytes.fromhex("e43b4322")
m3 = bytes.fromhex(sys.argv[1])

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(3.0)
client_socket.setsockopt(socket.SOL_SOCKET, 25, b'br0')
addr = ("192.168.200.21", 32108)

client_socket.sendto(m1, addr)
print("SEND: "+m1.hex())
try:
    # response 1
    data, server = client_socket.recvfrom(1024)
    print("RECV: "+data.hex())

    # request 2
    m2 = data
    client_socket.sendto(m2, server)
    print("SEND: "+m2.hex())

    # response 2
    data, server = client_socket.recvfrom(1024)
    print("RECV: "+data.hex())

    client_socket.sendto(m3, server)
    print("SEND: "+m3.hex())

    # response 3
    data, server = client_socket.recvfrom(1024)
    print("RECV: "+data.hex())

except socket.timeout:
    print('REQUEST TIMED OUT')

