from multiprocessing import Process,Pool,Queue
import os,time,random
import subprocess,threading

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

# def write(q):
#     print('%s running writing...' % os.getpid())
#     for i in ['A','B','C']:
#         print('write %s...' % i)
#         q.put(i)
#         time.sleep(random.random())
# def read(q):
#     print('%s running reading...' % os.getpid())
#     while True:
#         c = q.get(True)
#         print('read %s...' % c)

# if __name__ == '__main__':
#     q = Queue()
#     fw = Process(target=write,args=(q,))
#     fr = Process(target=read,args=(q,))
#     fw.start()
#     fr.start()
#     #等待fw结束
#     fw.join()
#     #fw结束,同时读完,强制结束fr
#     fr.terminate()

# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         print('thread %s >>> %s' % (threading.current_thread().name,n))
#         time.sleep(1)
#         n += 1
#     print('thread %s ended...' % threading.current_thread().name)

# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop,name='loopThread')
# t.start()
# t.join()
# print('thread %s ended...' % threading.current_thread().name)

# sum = 0
# def change(n):
#     global sum
#     sum += n
#     sum -= n

# def loop(n):
#     for i in range(1000000):
#         change(n)

# t1 = threading.Thread(target=loop,args=(5,))
# t2 = threading.Thread(target=loop,args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# #结果不一定为0
# print(sum)

# #加锁改进版
# sum = 0
# #获得锁
# lock = threading.Lock()
# def change(n):
#     global sum
#     sum += n
#     sum -= n

# def loop(n):
#     for i in range(1000000):
#         lock.acquire()
#         try:
#             change(n)
#         finally:
#             lock.release()

# t1 = threading.Thread(target=loop,args=(5,))
# t2 = threading.Thread(target=loop,args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(sum)

local = threading.local()

def process_name():
    name = local.name
    print('%s >>> %s' % (threading.current_thread().name,name))

def process_thread(name):
    local.name = name
    process_name()

t1 = threading.Thread(target=process_thread,args=("aa",),name="A_Thread")
t2 = threading.Thread(target=process_thread,args=("bb",),name="B_Thread")
t1.start()
t2.start()
t1.join()
t2.join()