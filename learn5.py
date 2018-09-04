#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


# if re.match(r'^\d{4}-\d{7}$','0797-2660012'):
#     print('true')
# else:
#     print('false')

# string = 'a  b c d     e'
# s = re.split(r'\s+',string)
# print(s)

# phone = '0797-2797012'
# m = re.match(r'(\d{4})-(\d{7})',phone)
# print(m)
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))
# print(m.groups())

# string = '1320000'
# #贪婪匹配,第一次匹配(\d+)把所有数字匹配了
# print(re.match(r'^(\d+)(0*)$',string).groups())
# print(re.match(r'^(\d+?)(0*)$',string).groups())

# #先编译好
# phone_re = re.compile(r'(\d{4})-(\d{7})')
# print(phone_re.match('0797-2660012').groups())

email_re = re.compile(r'(.+)@(\w+).([a-zA-z]+)')
print(email_re.match('someone@gmail.com').groups())
print(email_re.match('bill.gates@microsoft.com'))