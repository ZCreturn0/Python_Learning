#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket,threading

def tcpLink(sock,addr):
    buffer = []
    d = sock.recv(1024)
    sock.send(d.decode('utf-8').encode('utf-8'))
    sock.close()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8888))
s.listen(5)
print('服务启动')
while True:
    sock,addr = s.accept()
    print(addr)
    t = threading.Thread(target=tcpLink,args=(sock,addr))
    t.start()