#!/usr/bin/env python3
import time
import socket

m1 = bytes.fromhex("e43b4322")
r1 = bytes.fromhex("e4db36cd03233b4323311396e95c73f8ac1224b8e01c355b652ba53ca9cef0ab5c14c29e7b8eb48f4772913b7ea9dff4ad599e7b8eb48f4777cef0b8fd58c64d2feb49aebc018d37c92907599e620d7d6647661e2fb3fbcef32551ffee69065d1884aadd80c29387a9cb9e73ded6e01e304fdd8d3d8c3e40f18c3670d06208a342ed0ea12fea54ea51fa7ac0AAAAAAAAAA")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(3.0)
addr = ("192.168.200.21", 32108)

try:
    # HANDSHAKE STEP 1
    client_socket.sendto(m1, addr)
    print("SEND: "+m1.hex())
    # HANDSHAKE STEP 2
    data, server = client_socket.recvfrom(1024)
    print("RECV: "+data.hex())

    # HANDSHAKE STEP 3
    m2 = data
    client_socket.sendto(m2, server)
    print("SEND: "+m2.hex())
    data, server = client_socket.recvfrom(1024)
    print("RECV: "+data.hex())

    # SEND REQUEST
    client_socket.sendto(r1, server)
    print("SEND: "+r1.hex())
    data, server = client_socket.recvfrom(1024)
    print("RECV: "+data.hex())

except socket.timeout:
    print('REQUEST TIMED OUT')

