#-*-coding:utf-8-*-
print '举例看信息熵的熵增现象'
from math import log
print -1.0*log(1.0,2)
print -1.0*log(0.5,2)
print -1.8*log(0.25,2)
print '以上分别设类别1 2 4 而各类的概率分别为1 0.5 0.25，熵是递增的。'

import trees
myDat,labels=trees.createDataSet()
print myDat
print trees.calcShannonEnt(myDat)
myDat[0][-1]='unknown'
print trees.calcShannonEnt(myDat)

myDat,labels=trees.createDataSet()
print myDat
print '分割样本：',trees.splitData(myDat,1,1)

print trees.chooseBestFeatureToSplit(myDat)


print '看看决策树的效果：'
myDat,labels=trees.createDataSet()
myTree=trees.createTree(myDat,labels)
print myTree

print '查看绘图效果'
import treePlotter
treePlotter.createPlot()