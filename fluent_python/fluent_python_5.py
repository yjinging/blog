# -*- coding: utf-8 -*-
'''
以下的code基本来自《fluent python》一书，根据章节划分，每部分有明显的章节记号，每部分去掉注释可执行成功。
code的内容和书不是完全对应的，有缺失也有修改，以说明概念为目的。

包含如下
part5 控制流程
'''


#############################14.1#####################################
# import re
# RE_WORD=re.compile('\w+')
# class Sentence1:
#     def __init__(self,text):
#         self.text=text
#         self.words=RE_WORD.findall(text)
#
#     def __getitem__(self,index):
#         return self.words[index]
#
#     def __len__(self):
#         return len(self.words)
#
#     def __repr__(self):
#         return 'Sentence(%s)'%repr(self.text)
# s=Sentence1('"The time has come,"the Walrus said,')
# print s
# print list(s)
# for word in s:#Sentence实现了__getitem__，所以是可迭代的
#     print word
#
# s='ABC'#可迭代对象
# for char in s:#一种写法（s有迭代器）
#     print char
# it=iter(s)#构造迭代器it
# while True:#另一种写法，不断在迭代器上调用next
#     try:
#         print next(it)
#     except StopIteration:
#         del it
#         break
# print '迭代器自身也可以迭代'
# s3=Sentence1('Pigs can fly.')
# it=iter(s3)
# print it
# for i in range(len(s3)-2):
#     print next(it)
# print list(it)#it也可以迭代
# print iter(it)
# print list(iter(s3))#iter方法重新构建迭代器


#############################14.3#####################################
import re
RE_WORD=re.compile('\w+')

import json

















