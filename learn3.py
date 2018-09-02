#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import pdb
from io import StringIO,BytesIO
import os
import pickle
import json
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

# F = open('pickle.txt','rb')
# l = pickle.load(F)
# F.close()
# d = pickle.loads(l)
# print(d)
# #dict转为json对象
# j = json.dumps(d)
# print(d)
# #json对象转为dict
# p = json.loads(j)
# print(p)

# #对象转为json
# class Stu(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# #非类方法,不能为私有属性
# def forDumps(dmp):
#     return {
#         'name':dmp.name,
#         'age':dmp.age
#     }
# def forObj(dmp):
#     return Stu(dmp['name'],dmp['age'])
# s = Stu('aa',12)
# # j = json.dumps(s,default=forDumps)
# # print(j)
# #__dict__:属性写成键值对
# j = json.dumps(s,default=lambda obj: obj.__dict__)
# print(j)

# #json转为对象
# o = json.loads(j,object_hook=forObj)
# print(o)

#对中文进行JSON序列化,True:二进制,False:中文
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
