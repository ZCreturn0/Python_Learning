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

# #限制class实例能添加的属性
# class Student(object):
#     __slots__ = ('name','age')

# s = Student()
# s.name = 'aaa'
# s.age = 12
# #报错
# s.score = '50'

# class Stu(object):
#     __age = 12
#     #setter与getter方法同名
#     @property
#     def score(self):
#         return self.__score
    
#     @score.setter
#     def score(self,sc):
#         if sc > 100 or sc < 0:
#             raise TypeError('out of range')
#         self.__score = sc

#     #只读属性
#     @property
#     def age(self):
#         return self.__age

# s1 = Stu()
# s2 = Stu()
# s1.score = 60
# print(s1.score)

# #超出范围报错
# s2.score = 120
# print(s2.score)

# #__str__    __repr__
# class Stu(object):
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,name):
#         self.__name = name
#     def __str__(self):
#         return 'name:%s' % self.__name
#     __repr__ = __str__
# s = Stu()
# s.name = "aaa"
# print(s)

class CountTo100(object):
    def __init__(self):
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count > 99:
            raise StopIteration('no more counts')
        self.count += 1
        return self.count
    #cound be more:like[0:10:2]..
    def __getitem__(self,n):
        if isinstance(n,int):
            return n
        elif isinstance(n,slice):
            start = n.start
            stop = n.stop
            L = []
            for i in range(start,stop+1):
                L.append(i)
            return L
    #只有在没有某个属性时才会调用这个函数
    def __getattr__(self,attr):
        return "no such attr:%s" % attr
    def __call__(self):
        print("__call__() called")
c = CountTo100()
# for i in c:
#     print(i)
print(c[5])
print(c[5:10])
print(c.count)
print(c.score)
c()