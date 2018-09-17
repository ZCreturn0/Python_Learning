#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket,time

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto(b'aaaaa',('127.0.0.1',8888))
time.sleep(2)
#客户端recv
print(s.recv(1024).decode('utf-8'))
time.sleep(2)
s.close()