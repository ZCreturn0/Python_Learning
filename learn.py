#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functions import *
#from collections import Iterable,Iterator
import os
from functools import reduce
import functools
import datetime

#name = input('input your name:')
#print('hello',name)


#num = input('input a number:')
#if(int(num) > 0):
#    print('this number is over 0')
#else:
#    print('this number is below 0')


#用r''表示''内部的字符串默认不转义
#print(r'sdf\tdsf\nsfsdf')
#用'''...'''的格式表示多行内容
#print('''asdas...asddasd...asdasd''')       #没效果
#print('''asdas
#...asddasd
#...asdasd''')

#ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
#print(ord('6'))
#print(chr(54))

#print('中文'.encode('utf-8'))
#print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

#len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
#print(len('adf'))
#print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
#print(len('中文'.encode('utf-8')))

#格式化与C语言一致
#print('%s is %d years old'%('aaa',12))

#{0} ... {n} 表示参数个数    :后表示参数格式    .调用format函数
#print('{0} 保留三位小数是 {1:.3f}'.format(3.141592353,3.141592353))
#print('{0} 保留三位小数是 {1:.3f}'.format(3.141592353,3.141592353))

#list 相当于数组
#arr = ['a','b','c']
#print(arr)
#用len()函数可以获得list元素的个数
#print(len(arr))
#下标是负数表示从后获取,-1表示最后一个元素
#print(arr[-1])
#末尾添加用append
#arr.append('e')
#print(arr)
#insert插入到指定位置
#arr.insert(3,'d')
#print(arr)
#pop()删除末尾,pop(i)删除下标i
#arr.pop();
#print(arr)
#arr.pop(0)
#print(arr)

#tuple   不可变的list
#tp = (1,2,3)
#print(tp)

#(1)表示小括号运算,返回1,要与tuple区分,=>(1,)
#print((1))
#print((1,))

""" a = input('input a number:')
if (int(a) < 60):
    print('不及格')
elif (int(a) < 80):
    print('良好')
elif (int(a) < 90):
    print('优秀')
else:
    print('666') """

""" arr = ['a','b','c','d','e'];
for item in arr:
    print(item)

print(list(range(5)))       #0-4
sum = 0
for item in range(101):
    sum += item
print(sum)

n=0
m=0
while(n <= 100):
    m += n
    n += 1
print(m) """

""" dic = {'a':1,'b':2,'c':3}
for item in dic:
    print(item,' => ',dic[item])
dic.pop('a')
print(dic) """

#set做交并集
# set1 = set([1,2,3,4])
# set2 = set([2,4,8,6])
# print('交集:',set1 & set2)
# print('并集:',set1 | set2)

#把输入的数字输出16进制
# num = input('inmput a number to transform to hex:')
# print(hex(int(num)))

#导入外部函数
#print(myAbs(-10))
#数据类型不正确,会报错
#print(myAbs('A'))

#函数可返回多个值,事实是一个值(tuple)
#print(mutiReturns(-10,20))

#缺省参数
# print(defaultVar(10,3))
# print(defaultVar(10))

#默认参数为可变对象
# print(changebleDefaultVar())
# print(changebleDefaultVar())
# print(changebleDefaultVar())

#默认参数为不可变对象
# print(unchangeableDefaultVar())
# print(unchangeableDefaultVar())
# print(unchangeableDefaultVar())

#可变参数(参数个数不确定)
# print(uncertainVarNumber(1,2,3))
# print(uncertainVarNumber(1,2,3,4))
# print(uncertainVarNumber(*[2,5,9]))
# print(uncertainVarNumber(*(6,7,9)))

#关键字参数,传为dict
#keywordVar('aaa',12,city='Shenzhen')

#slice
#L[0:3] == L[:3]从0到3索引:   范围:[0,3)
# L = [0,1,2,3,4,5,6,7]
# print(L[0:3])
# print(L[3:6])
#从后取:最后一个为-1
#print(L[-3:-1])

#R = list(range(100))
#前10个
#print(R[:10])
#前10个每2个取一次
# print(R[:10:2])
#所有每2个取一次
# print(R[::2])

#tuple切片
#T = (0,1,2,3,4,5,6)
#print(T[:3])
#字符串切片
#print('adfgdfgdf'[:3])

""" print(trim('  regergerg   '),'end')
print(trim('  reger  gerg   '),'end')
print(trim('  reger gerg'),'end')
print(trim(''),'end') """

''' #dict遍历
D = {'a':1,'b':2,'c':3}
#遍历key
print('遍历key:')
for key in D:
    print(key,':',D[key])
#遍历value
print('遍历value:')
print(D.values())
for val in D.values():
    print(val)
#遍历key-value
print('遍历key-value:')
print(D.items())
for key,val in D.items():
    print(key,'-',val) '''

''' #字符串遍历
string = 'dsgdfhgsdfg'
for ch in string:
    print(ch)
#判断是否可迭代
print(isinstance(string,Iterable)) '''

''' L = ['A','B','C']
for index,val in enumerate(L):
    print(index,val) '''

#用迭代查找一个list中最小和最大值，并返回一个tuple
''' L = [5,2,6,7,9,1,4]
print(minAndMax(L)) '''

#10以内偶数平方
#print([x*x for x in range(1,11) if x % 2 == 0])
#嵌套列表
#9-9乘法表
#print([str(m)+'*'+str(n)+'='+str(m*n) for m in range(1,10) for n in range(m,10)])

''' #列出当前文件夹下所有文件
print([d for d in os.listdir('.')])

#把字符串转为小写,非字符串过滤
L1 = ['Hello', 'World', 18, 'Apple', None]
print([string.lower() for string in L1 if isinstance(string,str)]) '''

''' G = (x for x in range(1,11))
print(G)
for g in G:
    print(g) '''

''' #输出fac(i)
for i in range(1,11):
    print(fac(i))

#输出对应的值
for i in fac(10):
    print(i)

f = fac(10)
print(next(f))
print(next(f))
print(next(f))
print(next(f)) '''

''' F = fac(10)
while True:
    try:
        print('val:',next(F))
    except StopIteration as e:
        print('over:',e.value)
        break '''

''' #可迭代对象
print(isinstance([],Iterable))
print(isinstance((x for x in range(1,11)),Iterable))

#迭代器
print(isinstance([],Iterator))
print(isinstance((x for x in range(1,11)),Iterator))
print(isinstance(iter([]),Iterator)) '''

#print(absAdd(-10,5,abs))
''' L = [1,5,-4,6,-7,4]
print(*map(abs,L))
print(reduce(add,L)) '''

''' L1 = ['adam', 'LISA', 'barT']
print(*map(firstCapital,L1))

L2 = [1,3,5,6,4,7,9,8,12]
print(*filter(isEven,L2)) '''

""" #按绝对值比较大小
print(sorted([36, 5, -12, 9, -21], key=abs))
#按绝对值比较大小反响排序
print(sorted([36, 5, -12, 9, -21], key=abs,reverse=True))

#按成绩排序
def getScore(stu):
    return stu[1]
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L,key=getScore)) """

""" #装饰器
def dec(text):
    def log(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s()' % (text,func.__name__))
            func(*args,**kw)
        return wrapper
    return log

@dec('call')
def hello(name1,name2,key="name"):
    print('hello',name1,name2)

hello('aaa','bbb',"ccc")
print(hello.__name__) """

""" #当前时间戳
print(datetime.datetime.now().timestamp()) """

#装饰器,显示func执行时间
# def logTime(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kw):
#         start = datetime.datetime.now().timestamp()
#         func(*args,**kw)
#         end = datetime.datetime.now().timestamp()
#         print('%s() ran over in %f s' % (func.__name__,end-start))
#     return wrapper

# @logTime
# def addSum(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum += i
#     print('sum is',sum)

# addSum(10)
# addSum(100000)
# addSum(10000000)

#偏函数
print(int('1011'))
print(int('1011',base=2))
#用偏函数生成一个专门处理二进制的函数
int2 = functools.partial(int,base=2)
print(int2('1011'))
#生成的函数仍可以传缺省参数
print(int2('1011',base=8))