#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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