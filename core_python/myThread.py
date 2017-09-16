# -*- coding: utf-8 -*-
import threading
from time import sleep,ctime

class MyThread(threading.Thread):#一个通用的Thread子类，可指定方法和方法的参数
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)#必须先调用基类的构造函数
        self.name=name
        self.func=func
        self.args=args

    def getResult(self):
        return self.res

    def run(self):#写run方法
        print 'starting',self.name,'at:',ctime()
        self.res=self.func(*self.args)#args为元组
        print self.name,'finished at:',ctime()