from multiprocessing import Process
import os

def child_func(arg):
    print('arg:%s   pid:%s' % (arg,os.getpid()))

if __name__ == '__main__':
    print("parent:%s" % os.getpid())
    #创建子进程
    p = Process(target=child_func,args=('child',))
    print('child start')
    p.start()
    p.join()
    print('child end')