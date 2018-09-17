#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket,time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8888))
s.send(b'aaaa')
time.sleep(1)
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
print(b''.join(buffer))
time.sleep(2)
s.close()