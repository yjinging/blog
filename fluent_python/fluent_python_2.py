# -*- coding: utf-8 -*-

'''
以下的code基本来自《fluent python》一书，根据章节划分，每部分有明显的章节记号，每部分去掉注释可执行成功。
code的内容和书不是完全对应的，有缺失也有修改，以说明概念为目的。

包含如下
part1 序幕 
part2 数据结构
'''

#############################1.1######################################
# import collections
#
# Card = collections.namedtuple('Card', ['rank', 'suit'])#命名元组
#
#
# class FrenchDeck:
#     ranks = [str(n) for n in range(2, 11)] + list('JQKA')
#     suits = 'spades diamonds clubs hearts'.split()  # 按照黑桃、方块、梅花、红桃的顺序
#
#     def __init__(self):
#         self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]#列表推导
#
#     def __len__(self):
#         return len(self._cards)
#
#     def __getitem__(self, position):
#         return self._cards[position]
#
# beer_card=Card('7','diamonds')
# print beer_card
# deck=FrenchDeck()
# print len(deck)
# print deck[0]#因为有了__getitem__方法，故可以直接用index方式调用__getitem__
#
# from random import choice
# print 'choice:',choice(deck)#有了__getitem__，可以方便地利用python标准库
#
# print deck[:3] #切片操作
# print deck[12::13]
#
#
# #按大小、花色从小到大排序打印
# suit_values=dict(spades=3,hearts=2,diamonds=1,clubs=0)
# def spades_high(card):
#     rank_value=FrenchDeck.ranks.index(card.rank)#数字的排位
#     return rank_value*len(suit_values)+suit_values[card.suit]#数字的排位＊花色种数＋花色排位
# print 'sorted:'
# for card in sorted(deck,key=spades_high):
#     print card
#
# #逆序输出
# print 'reversed:'
# for card in reversed(deck):
#     print card


#############################1.2######################################
# from math import hypot
# class Vector:
#     def __init__(self,x=0,y=0):
#         self.x=x
#         self.y=y
#
#     def __repr__(self):
#         return 'Vector(%r,%r)'%(self.x,self.y)
#
#     # def __str__(self):
#     #     return 'Vector(%r,%r)'%(self.x,self.y)
#
#     def __abs__(self):
#         return hypot(self.x,self.y)
#
#     def __bool__(self):
#         return bool(abs(self))
#
#     def __add__(self, other):
#         x=self.x+other.x
#         y=self.y+other.y
#         return Vector(x,y)
#
#     def __mul__(self, scalar):
#         return Vector(self.x*scalar,self.y*scalar)
#
# print 'examples on dunder method:'
# v1=Vector(2,4)
# v2=Vector(2,1)
# print v1+v2 #调用特殊方法__add__和__repr__
# print abs(v1+v2) #调用特殊方法__abs__
# print (v1+v2)*2  #调用特殊方法__mul__和__repr__
# print bool(v1+v2)  #调用特殊方法__bool__


#############################2.2######################################
# symbols='$%^&*(aA123'
# codes=[ord(symbol) for symbol in symbols]#列表推导(list comprehension)
# print codes
#
# beyond_ascii=[ord(s) for s in symbols if ord(s)>50]#列表推导
# print beyond_ascii
# beyond_ascii=list(filter(lambda c:c>50,map(ord,symbols))) #map&filter
# print beyond_ascii
#
# colors=['black','white']
# sizes=['S','M','L']
# tshirts=[(color,size) for color in colors for size in sizes]#列表推导计算笛卡尔积
# print tshirts
#
# #生成器表达式和列表推导的语法差不多，前者是圆括号，后者是方括号
# symbols='$%^&*(aA123'
# print tuple(ord(symbol) for symbol in symbols) #生成器表达式生成元祖
# import array
# print array.array('I',(ord(symbol) for symbol in symbols))#生成器表达式生成数组
#
# colors=['black','white']
# sizes=['S','M','L']
# for tshirt in ('%s %s'%(c,s) for c in colors
#                              for s in sizes):#用生成器表达式实现笛卡尔积
#     print tshirt


#############################2.3######################################
# #元组
# lax_coordinates=(33.9425,-118.408056)
# city,year,pop,chg,area=('Tokyo',2003,32450,0.66,8014)
# traveler_ids=[('USA','31195855'),('BRA','CE342567'),('ESP','XDA205856')]
# for passport in sorted(traveler_ids):
#     print ('%s/%s'%passport)#元组自动拆包，故%运算符能被匹配到对应的元组元素上
# for country,_ in traveler_ids:#拆包
#     print country
#
# print '*运算符把一个可迭代对象拆开作为函数的参数'
# print divmod(20,8)#divmod为除法的结果及余数
# t=(20,8)
# print divmod(*t)#*运算符把一个可迭代对象拆开作为函数的参数
#
# print '元组用于路径和文件名分割示例'
# import os
# _,filename=os.path.split('/home/yujing/.ssh/idrsa.pub')
# print _,filename
#
# #具名元组
# print '具名元组的属性和方法'
# from collections import namedtuple
# city=namedtuple('City','name country population coordinates')
# tokyo=city('Tokyo','JP',36,(35,139))
# print tokyo
# print city._fields
# LatLong=namedtuple('LatLong','lat long')
# delhi_data=('Delhi NCR','IN',21.9,LatLong(28,77))
# delhi=city._make(delhi_data)#city._make(delhi_data)的作用跟city(*delhi_data)一样
# print delhi._asdict()
# delhi2=city(*delhi_data)
# print delhi2._asdict()


#############################2.4######################################
# #切片
# s='bicycle'
# print s[::3]#s[a:b:c]对s在a和b之间以c为间隔取值
# print s[::-1]#负值指反向取值
# l=list(range(10))
# print l
# l[2:5]=[20,30]#切除或就地修改
# print l
# l[5:7]=[11,12]
# print l
# l[2::2]=[100,101,102,103]
# print l
# print l*2#用＋和＊基于已有列表生成新列表
# print l+l


#############################3.1######################################
# #可散列对象要实现__hash__方法和__qe__方法
# tt=(1,2,(30,40))#所有元素可散列，故元组tt可散列
# print hash(tt)
# tf=(1,2,frozenset([30,40]))#frozenset里都是可散列的
# print hash(tf)
# tl=(1,2,[30,40])#list不是可散列的，故tl不是可散列的
# print hash(tl)

