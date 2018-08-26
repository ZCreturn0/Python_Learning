#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# a file providers some functions
def myAbs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('wrong type')
    return x if x>0 else -x     #  replace  return x > 0 ? x : -x



def mutiReturns(x,y):
    return x+10,y+10

#缺省参数
def defaultVar(x,n=2):
    return x*n

#默认参数为可变对象
def changebleDefaultVar(L=[]):
    L.append('A')
    return L

#默认参数为不可变对象
def unchangeableDefaultVar(L=None):
    if(L==None):
        L = []
    L.append('A')
    return L

#可变参数(参数个数不确定)
def uncertainVarNumber(*args):
    sum = 0
    for items in args:
        if not isinstance(items,(int,float)):
            raise TypeError('wrong type')
        sum += items
    return sum

#关键字参数,传为dict
def keywordVar(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)