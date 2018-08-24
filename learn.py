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