# -*- coding: utf-8 -*-
'''
以下的code基本来自《fluent python》一书，根据章节划分，每部分有明显的章节记号，每部分去掉注释可执行成功。
code的内容和书不是完全对应的，有缺失也有修改，以说明概念为目的。

包含如下
part3　把函数视作对象
'''

#############################5.1######################################
# def factorial(n):
#     '''return n!'''
#     return 1 if n <2 else n*factorial(n-1)
# print factorial(5)
# print 'func_code:'
# print factorial.func_code
# print '__doc__'
# print factorial.__doc__#__doc__是函数对象的众多属性之一
# print type(factorial)
# print help(factorial)
#
# print '通过别的名称使用函数，再把函数作为参数传递'
# fact=factorial
# print fact(5)
# print map(factorial,range(11))
# print list(map(fact,range(11)))


#############################5.2######################################
# #高阶函数
# def factorial(n):
#     '''return n!'''
#     return 1 if n <2 else n*factorial(n-1)
# fact=factorial
# print '接受函数为参数，或者把函数作为结果返回的函数，是高阶函数'
# fruits=['strawberry','fig','apple','cherry','raspberry','banana']
# print sorted(fruits,key=len)
# print sorted(fruits,key=reversed)
# def reverse(s):
#     return s[::-1]
# print sorted(fruits,key=reverse)
#
# #map、filter与列表推导比较
# print 'map/filter VS 列表推导'
# print list(map(fact,range(6)))
# print [fact(n) for n  in range(6)]
# print list(map(factorial,filter(lambda n:n%2,range(6))))
# print [factorial(n) for n in range(6) if n%2]
#
# from functools import reduce
# from operator import add
# print reduce(add,range(100))#reduce and sum
# print sum(range(100))#sum把求得操作连续应用到序列的元素上并归约，和上一行等价


#############################5.3######################################
# fruits=['strawberry','fig','apple','cherry','raspberry','banana']
# print sorted(fruits,key=lambda word:word[::-1])#lambda表达式创建函数对象
# def factorial(n):
#      '''return n!'''
#      return 1 if n <2 else n*factorial(n-1)
# print callable(factorial)#判断对象能否调用


#############################5.5######################################
# import random
# class BingoCage:
#     def __init__(self,items):
#         self._items=list(items)
#         random.shuffle(self._items)
#
#     def pick(self):
#         try:
#             return self._items.pop()
#         except IndexError:
#             raise LookupError('pick from empty BingoCage')
#
#     def __call__(self):#实现__call__方法可用来创建函数类对象
#         return self.pick()
#
# bingo=BingoCage(range(3))
# print bingo.pick(),bingo(),bingo()#函数类对象，直接调用对象名


#############################5.6######################################
# def factorial(n):
#      '''return n!'''
#      return 1 if n <2 else n*factorial(n-1)
# print dir(factorial)#列出factorial的所有属性
#
# class C:pass
# obj=C()
# def func():pass
# sorted(set(dir(func))-set(dir(obj)))#打印函数有而对象没有的属性






























