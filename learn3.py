#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import pdb
from io import StringIO,BytesIO
#debug，info，warning，error
logging.basicConfig(level=logging.INFO)

# def foo(num):
#     assert num != 0,'num is 0'
#     return 10 / num
# print(foo(2))
#print(foo(0))

# logging.info('---calc:---')
# logging.error(10/0)

# s= '0'
# n = int(s)
# pdb.set_trace()
# print(10/n)

#读文件
# try:
#     f = open('text.txt','r')
#     print(f.read())
# except IOError as e:
#     print(e)
# finally:
#     f.close()

#另一种读文件方法
# with open('text.txt','r') as f:
# #    print(f.read())
#     print('-------------')
#     l = f.readlines()
#     print(l)

# with open('write.txt','w',encoding='utf-8') as f:
#     f.write('aaa')
#     f.close()
# with open('write.txt','a',encoding='utf-8') as F:
#     F.write('bbb')
#     F.close()

#StringIO
# s = StringIO()
# s.write('aaa')
# s.write('bbb')
# s.write('ccc')
# print(s.getvalue())

# S = StringIO(s.getvalue())
# while True:
#     ss = S.readline()
#     if ss == '':
#         break
#     print(ss)

#ByteIO
b = BytesIO()
b.write('666'.encode('utf-8'))
print(b.getvalue())

B = BytesIO(b.getvalue())
print(B.read())