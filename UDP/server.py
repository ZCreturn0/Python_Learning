#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',8888))
while True:
    #服务端recvfrom
    data,addr = s.recvfrom(1024)
    print('接收来自%s:%s的数据' % addr)
    s.sendto(b'%s?????' % data,addr)