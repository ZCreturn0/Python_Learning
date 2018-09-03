from multiprocessing import Process,Pool,Queue
import os,time,random
import subprocess

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

# print('ping www.python.org:')
# r = subprocess.call(['ping','www.python.org'])
# print('return code:',r)

def write(q):
    print('%s running writing...' % os.getpid())
    for i in ['A','B','C']:
        print('write %s...' % i)
        q.put(i)
        time.sleep(random.random())
def read(q):
    print('%s running reading...' % os.getpid())
    while True:
        c = q.get(True)
        print('read %s...' % c)

if __name__ == '__main__':
    q = Queue()
    fw = Process(target=write,args=(q,))
    fr = Process(target=read,args=(q,))
    fw.start()
    fr.start()
    #等待fw结束
    fw.join()
    #fw结束,同时读完,强制结束fr
    fr.terminate()