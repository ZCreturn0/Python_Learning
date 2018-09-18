#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import poplib

email = input('email:')
password = input('password:')
pop3_server = input('server:')

server = poplib.POP3(pop3_server)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))

server.user(email)
server.pass_(password)

