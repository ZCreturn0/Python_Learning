#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#定义学生类
class Student(object):
    #初始化
    def __init__(self,name,score):
        #__开头表示私有变量,但同时__表示特殊变量,外部可访问
        self.__name = name
        self.__score = score
    
    #输出
    def print_score(self):
        print(self.__name,'got',self.__score)

a = Student('aa',69)
a.print_score()