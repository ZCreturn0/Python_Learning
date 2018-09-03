from multiprocessing import Process
import os,time.random

# def child_func(arg):
#     print('arg:%s   pid:%s' % (arg,os.getpid()))

# if __name__ == '__main__':
#     print("parent:%s" % os.getpid())
#     #创建子进程
#     p = Process(target=child_func,args=('child',))
#     print('child start')
#     p.start()
#     p.join()
#     print('child end')

def multiPrecessingCallback(num):
    print('task%s,pid:%s' % (num,os.getpid()))
    strat = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('task%s runs in %.2fs' % (num,end-start))

