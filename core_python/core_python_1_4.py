# -*- coding: utf-8 -*-
'''
以下的code基本来自《core python》一书，根据章节划分，每部分有明显的章节记号，每部分去掉注释可执行成功。
code的内容和书不是完全对应的，有缺失也有修改，以说明概念为目的。

包含如下
第４章　多线程编程
'''

############################示例4.2#####################################
# import thread
# from time import sleep,ctime
# def loop0():
#     print 'start loop 0 at:',ctime()
#     sleep(4)
#     print 'loop 0 done at:',ctime()
#
# def loop1():
#     print 'start loop 1 at:',ctime()
#     sleep(2)
#     print 'loop 1 done at:',ctime()
#
# def main():#用额外延时的方式限制
#     print 'starting at:',ctime()
#     thread.start_new_thread(loop0,())
#     thread.start_new_thread(loop1,())
#     sleep(5)#主程序退出时各线程被强制退出。可以试试sleep参数为0，3，4，5的情况
#     print 'all done at:',ctime()
#
# if __name__=='__main__':
#     main()


############################示例4.3#####################################
# import thread
# from time import sleep, ctime
# loops = [4, 2]
# def loop(nloop, nsec, lock):
#     print 'start loop', nloop, 'at:', ctime()
#     sleep(nsec)
#     print 'loop', nloop, 'done at:', ctime()
#     lock.release()
#
# def main():
#     print 'starting at:', ctime()
#     locks = []
#     nloops = range(len(loops))
#     for i in nloops:
#         lock = thread.allocate_lock(); lock.acquire(); locks.append(lock)
#     for i in nloops:
#         thread.start_new_thread(loop, (i, loops[i], locks[i]))#为每个线程创建一个锁，各个线程执行完释放锁。
#     for i in nloops:
#         while  locks[i].locked(): pass#相比示例4.2设定一个deadline，耗时更少，效率更高。
#     print 'all done at:', ctime()
#
# if __name__ == '__main__':
#     main()


############################示例4.4#####################################
# #整个python程序将在所有非守护线程退出之后才退出
# #即：主线程将在所有非守护线程退出之后才退出
# #使用threading模块的方法1：创建Thread的实例，传给它一个函数
# import threading
# from time import sleep,ctime
# loops=[4,2]
# def loop(nloop,nsec):
#     print 'start loop',nloop,'at:',ctime()
#     sleep(nsec)
#     print 'loop',nloop,'done at:',ctime()
#
# def main():
#     print 'starting at:',ctime()
#     threads=[]
#     nloops=range(len(loops))
#     for i in nloops:
#         t=threading.Thread(target=loop,args=(i,loops[i]))#target：函数　args：函数的参数
#         threads.append(t)
#     for i in nloops:
#         threads[i].start()
#     for i in nloops:
#         threads[i].join()#在线程thread[i]终止之前一直挂起。故join又称为自旋锁
#     print 'all done at',ctime()
# if __name__=='__main__':
#     main()


############################示例4.5#####################################
# #使用threading模块的方法2：创建Thread的实例，传给它一个可调用的类的实例。这种方式更有面向对象风格
# import threading
# from time import sleep,ctime
# loops=[4,2]
# class ThreadFunc(object):
#     def __init__(self,func,args,name=''):
#         self.name=name
#         self.func=func
#         self.args=args
#
#     def __call__(self):
#         self.func(*self.args)
#
# def loop(nloop,nsec):
#     print 'start loop',nloop,'at:',ctime()
#     sleep(nsec)
#     print 'loop',nloop,'done at:',ctime()
#
# def main():
#     print 'starting at:',ctime()
#     threads=[]
#     nloops=range(len(loops))
#     for i in nloops:
#         t=threading.Thread(target=ThreadFunc(loop,(i,loops[i]),loop.__name__))#target：类的实例。函数名、函数参数、name都作为类实例初始化的参数
#         threads.append(t)
#     for i in nloops:
#         threads[i].start()#会调用__call__方法
#     for i in nloops:
#         threads[i].join()
#     print 'all done at:',ctime()
# if __name__=='__main__':
#     main()


############################示例4.6#####################################
# #使用threading模块的方法3：派生Thread的子类，并创建子类的实例
# import threading
# from time import sleep,ctime
# loops=[4,2]
# class MyThread(threading.Thread):
#     def __init__(self,func,args,name=''):
#         threading.Thread.__init__(self)#必须先调用基类的构造函数
#         self.name=name
#         self.func=func
#         self.args=args
#
#     def run(self):#写run方法
#         self.func(*self.args)
#
# def loop(nloop,nsec):
#     print 'start loop',nloop,'at:',ctime()
#     sleep(nsec)
#     print 'loop',nloop,'done at:',ctime()
#
# def main():
#     print 'starting at:',ctime()
#     threads=[]
#     nloops=range(len(loops))
#     for i in nloops:
#         t=MyThread(loop, (i, loops[i]), loop.__name__)
#         threads.append(t)
#     for i in nloops:
#         threads[i].start()
#     for i in nloops:
#         threads[i].join()
#     print 'all done at:',ctime()
#
# if __name__=='__main__':
#     main()


############################示例4.8#####################################
# from myThread import MyThread
# from time import ctime,sleep
# def fib(x):
#     sleep(0.005)
#     if x<2:return 1
#     return (fib(x-2)+fib(x-1))
# def fac(x):
#     sleep(0.1)
#     if x<2:return 1
#     return x*fac(x-1)
# def sum(x):
#     sleep(0.1)
#     if x<2:return 1
#     return x+sum(x-1)
#
# funcs=[fib,fac,sum]
# n=12
#
# def main():
#     nfuncs=range(len(funcs))
#     print 'single thread:'
#     for i in nfuncs:
#         print 'starting',funcs[i].__name__,'at:',ctime()
#         print funcs[i](n)
#         print funcs[i].__name__,'finished at:',ctime()
#     print 'multiple threads:'
#     threads=[]
#     for i in nfuncs:
#         t=MyThread(funcs[i],(n,),funcs[i].__name__)#注意此处必须用(n,)而不是(n),前者表示它是一个元组，后者只是一个变量。
#         threads.append(t)
#     for i in nfuncs:
#         threads[i].start()
#     for i in nfuncs:
#         threads[i].join()
#         print threads[i].getResult()
#
# if __name__=='__main__':
#     main()

















