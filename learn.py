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
print(ord('6'))
print(chr(54))

print('中文'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

#len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
print(len('adf'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

#格式化与C语言一致
print('%s is %d years old'%('aaa',12))

#{0} ... {n} 表示参数个数    :后表示参数格式    .调用format函数
print('{0} 保留三位小数是 {1:.3f}'.format(3.141592353,3.141592353))
print('{0} 保留三位小数是 {1:.3f}'.format(3.141592353,3.141592353))