# -*- coding: utf-8 -*-
'''
以下的code基本来自《fluent python》一书，根据章节划分，每部分有明显的章节记号，每部分去掉注释可执行成功。
code的内容和书不是完全对应的，有缺失也有修改，以说明概念为目的。

包含如下
part4　面向对象惯用法
'''



#############################8.1######################################
# print 'python变量类似于Java中的引用式变量'
# a=[1,2,3]
# b=a
# a.append(4)
# print b#a和b引用同一个列表
#
# charles={'name':'Charles L.Dodgson','born':1832}
# lewis=charles
# print lewis is charles#lewis是charles的别名。is运算符比较两个对象的标识
# print id(lewis),id(charles)#id()函数返回对象标识的整数表示
# alex={'name':'Charles L.Dodgson','born':1832}
# print alex==charles,alex is charles#“==”实际调用的是dict的__eq__方法，而dict的__eq__方法是比较对象的值
# print alex is not charles
# print alex is None


#############################8.3######################################
# #浅复制和深复制
# class Bus:
#     def __init__(self,passengers=None):
#         if passengers is None:
#             self.passengers=[]
#         else:
#             self.passengers=list(passengers)
#
#     def pick(self,name):
#         self.passengers.append(name)
#
#     def drop(self,name):
#         self.passengers.remove(name)
#
# import copy
# bus1=Bus(['Alice','Bill','Claire','David'])
# bus2=copy.copy(bus1)
# bus3=copy.deepcopy(bus1)
# print id(bus1),id(bus2),id(bus3)
# print id(bus1.passengers),id(bus2.passengers),id(bus3.passengers)#bus2是浅拷贝来的，故其passengers拷贝的是引用
# bus1.drop('Bill')
# print bus2.passengers
# print bus3.passengers
#
# a=[10,20]
# b=[a,30]
# a.append(b)
# print a
# from copy import deepcopy
# c=deepcopy(a)
# print c


#############################8.5######################################
# import weakref
# a_set={0,1}
# wref=weakref.ref(a_set)
# print wref
# print wref()
# a_set={2,3,4}
# print wref()
#
#
# s1={1,2,3}
# s2=s1
# def bye():
#     print 'Gone with the wind...'
# ender=weakref.finalize(s1,bye)#python2.7的weakref没有finalize函数？运行总是报错
# print ender.alive
# del s1
# print ender.alive
# s2='spam'
# print ender.alive
