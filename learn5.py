#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
#从datetime模块带入datetime类
import time
from datetime import datetime,timedelta
from collections import namedtuple,deque,defaultdict,OrderedDict,Counter
import base64
import hashlib
import hmac
from contextlib import contextmanager
from urllib import request,parse
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

# now = datetime.now()
# print(now)
# print(now+timedelta(hours=10))

# p = namedtuple('Point',['x','y'])
# p.x = 1
# p.y = 2
# print(p)

# d = deque(['a','b','c'])
# d.append('d')
# d.appendleft('y')
# print(d)
# d.popleft()
# print(d)

# #key不存在返回默认
# d = defaultdict(lambda:'N/A')
# d['x'] = 1
# d['y'] = 2
# print(d['x'])
# print(d['y'])
# print(d['z'])

# od = OrderedDict([('a',1),('b',2),('c',3)])
# print(od)
# #按添加顺序排序
# od['f'] = 6
# od['d'] = 4
# print(od)

# c = Counter()
# string = 'dafgadfgsdfgsdfgfdgasaseerttyuty'
# for ch in string:
#     c[ch] += 1      #c['d']  c['a']  ....
# print(c)

# print(base64.b64encode('撒旦法'.encode('utf-8')))
# print(base64.urlsafe_b64encode('撒旦法'.encode('utf-8')))

# #md5加密,一个32位的16进制
# md5 = hashlib.md5()
# md5.update('asd'.encode('utf-8'))
# md5.update('afe'.encode('utf-8'))
# print(md5.hexdigest())

# #sha1加密,一个40位的16进制
# sha1 = hashlib.sha1()
# sha1.update('aaa'.encode('utf-8'))
# sha1.update('bbb'.encode('utf-8'))
# print(sha1.hexdigest())

# #私钥
# key = b'zc'
# #明文
# msg = b'a message'
# h = hmac.new(key,msg,digestmod='md5')
# print(h.hexdigest())

# #从10开始迭代
# n = itertools.count(10)
# for i in n:
#     print(i)
#     time.sleep(0.01)

# c = itertools.cycle('ABCDEF')
# for i in c:
#     print(i)
#     time.sleep(0.1)

# r = itertools.repeat('ABC',3)
# for i in r:
#     print(i)

# n = itertools.count(1)
# ns = itertools.takewhile(lambda x:x<=10,n)
# for i in ns:
#     print(i)

# for i in itertools.chain([1,2,3],(2,6,8)):
#     print(i)

# #必须是相邻的
# for key,group in itertools.groupby([1,-6,6,3,-2,-6,-3],lambda x:abs(x)):
#     print(key,list(group))

# class Query(object):
#     def __init__(self,string):
#         self.string = string
#     # def __enter__(self):
#     #     print('-----enter-----')
#     #     return self
#     # def __exit__(self, exc_type, exc_value, traceback):
#     #     print('-----exit-----')
#     def query(self):
#         print(self.string)
# # with Query('666') as q:
# #     q.query()

# @contextmanager
# def create_query(string):
#     print('-----enter-----')
#     q = Query(string)
#     yield q
#     print('-----exit-----')
# with create_query('666') as q:
#     q.query()

# @contextmanager
# def htmlTemplate(tag):
#     print('<%s>' % tag)
#     yield
#     print('</%s>' % tag)
# with htmlTemplate('h1'):
#     print('content')

# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     print('Status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print('%s:%s' % (k,v))
#     data = f.read()
#     print('Data:')
#     print(data.decode('utf-8'))

# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent','Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1')
# with request.urlopen(req) as f:
#     print('Status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print('%s:%s',(k,v))
#     print(f.read().decode('utf-8'))

phone = input('your phone:')
password = input('your password:')
login_data = parse.urlencode([
    ('username',phone),
    ('password',password),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])
req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin','https://weibo.com')
req.add_header('Referer','https://weibo.com/')
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
with request.urlopen(req,data=login_data.encode('utf-8')) as r:
    print(r.read().decode('utf-8'))