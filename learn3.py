#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import pdb
from io import StringIO,BytesIO
import os
import pickle
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
# b = BytesIO()
# b.write('666'.encode('utf-8'))
# print(b.getvalue())

# B = BytesIO(b.getvalue())
# print(B.read())

#查看系统:
#print(os.name)
#uname()函数在Windows上不提供
#print(os.uname())
#print(os.environ)
# print(os.environ.get('PATH'))

#查看当前目录的绝对路径:
#print(os.path.abspath('.'))

# #在某个目录下创建一个新目录:
# #1.创建路径
# path = os.path.join(os.path.abspath('.'),'newDir')
# #2创建目录
# os.mkdir(path)

# #删除目录:
# os.rmdir(path)

# print([x for x in os.listdir('.')])
# #列出当前目录下所有文件夹:
# print([x for x in os.listdir('.') if os.path.isdir(x)])
# #列出当前目录下所有扩展名为'.py'的文件
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

# d = dict(aa='aa',bb='bb',cc='cc')
# D = pickle.dumps(d)
# print(D)

# f = open('pickle.txt','wb')
# pickle.dump(D,f)
# f.close()

F = open('pickle.txt','rb')
l = pickle.load(F)
F.close()
print(pickle.loads(l))
