#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' #定义学生类
class Student(object):
    #类属性
    likeStatic = 'static'
    count = 0
    #初始化
    def __init__(self,name,score):
        #__开头表示私有变量,但同时__表示特殊变量,外部可访问
        self.__name = name
        self.__score = score
        Student.count += 1
    
    #输出
    def print_score(self):
        print(self.__name,'got',self.__score)

a = Student('aa',69)
a.print_score()

#调用类属性
print(a.likeStatic)
print(Student.likeStatic)

#创建实例自己的属性
a.likeStatic = 'a_static'

#a的属性比类属性级别高,覆盖类属性
print(a.likeStatic)
#类属性
print(Student.likeStatic)

#删除自身属性
del a.likeStatic
#输出类属性
print(a.likeStatic)

print(Student.count)
b = Student('bb',69)
c = Student('cc',69)
d = Student('dd',69)
print(Student.count)

#print(type(a))
#print(dir(a)) '''

class Student(object):
    __slots__ = ('name','age')

s = Student()
s.name = 'aaa'
s.age = 12
#报错
s.score = '50'