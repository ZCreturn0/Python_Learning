#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
#从datetime模块带入datetime类
from datetime import datetime,timedelta


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

# email_re = re.compile(r'(.+)@(\w+).([a-zA-z]+)')
# print(email_re.match('someone@gmail.com').groups())
# print(email_re.match('bill.gates@microsoft.com'))

# print(datetime.now())
# print(type(datetime.now()))

# print(datetime(2018,12,10,10,11))
# #timestamp
# print(datetime.now().timestamp())

# print(datetime.fromtimestamp(datetime.now().timestamp()))

# #本地时间转UTC时间
# print(datetime.utcfromtimestamp(datetime.now().timestamp()))

# #str转时间
# print(datetime.strptime('2018-01-12 12:11:10','%Y-%m-%d %H:%M:%S'))
# #时间转str
# print(datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S'))

now = datetime.now()
print(now)
print(now+timedelta(hours=10))