from multiprocessing import Process,Pool
import os,time,random

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

# def multiPrecessingCallback(num):
#     print('task%s,pid:%s' % (num,os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('task%s runs in %.2fs' % (num,end-start))

# if __name__ == '__main__':
#     print('parent:%s' % os.getpid())
#     #建立进程池,最多跑4个进程(默认个数为CPU个数)
#     p = Pool(4)
#     for  i in range(5):
#         p.apply_async(multiPrecessingCallback,args=(i,))
#     print('wait for running:')
#     #close后不能再添加进程
#     p.close()
#     #join等待进程执行完毕
#     p.join()
#     print('now,over')



