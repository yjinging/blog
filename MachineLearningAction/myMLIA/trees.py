#-*-coding:utf-8-*-
'''
Created on Sep 17, 2017
tree: Decision Tree

Input:      inX: vector to compare to existing dataset (1xN)
            dataSet: size m data set of known vectors (NxM)
            labels: data set labels (1xM vector)
            k: number of neighbors to use for comparison (should be an odd number)

Output:     the most popular class label

@author: yujingbaobao
'''
from math import log
def calcShannonEnt(dataSet):
    '''
    :param dataSet: 
    :return: 以dataSet的最后一列为标签值，求出该数据集的熵
    '''
    numEntries=len(dataSet)
    labelCounts={}
    for featVec in dataSet:
        currentLabel=featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1
    shannonEnt=0.0
    for key in labelCounts.keys():
        prob=float(labelCounts[key])/numEntries
        shannonEnt-=prob*log(prob,2)
    return shannonEnt

def createDataSet():
    dataSet=[[1,1,'yes'],
             [1,1,'yes'],
             [1,0,'no'],
             [0,1,'no'],
             [0,1,'no']]
    labels=['no surfacing','flippers']
    return dataSet,labels

def splitData(dataSet,axis,value):
    '''用某个特征划分数据集，将特征值等于指定值的的样本返回'''
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis]==value:
            reducedFeatVec=featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    numFeatures=len(dataSet[0])-1
    baseEntropy=calcShannonEnt(dataSet)
    bestInfoGain=0.0;bestFeature=-1
    for i in range(numFeatures):
        featList=[example[i] for example in dataSet]
        uniqueVals=set(featList)#从列表中创建集合可快速得到列表唯一元素值
        newEntropy=0.0
        for value in uniqueVals:
            subDataSet=splitData(dataSet,i,value)
            prob=len(subDataSet)/float(len(dataSet))
            newEntropy+=prob*calcShannonEnt(subDataSet)
        infoGain=baseEntropy-newEntropy
        if(infoGain>bestInfoGain):
            bestInfoGain=infoGain
            bestFeature=i
    return bestFeature

import operator
def majorityCnt(classList):
    '''投票工具。统计classList里出现最多的元素并返回'''
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():classCount[vote]=0
        classCount[vote]+=1
    sortedClassCount=sorted(classCount.iteritems(),
                            key=operator.itemgetter(1),
                            reverse=True)
    return sortedClassCount[0][0]

def createTree(dataSet,labels):
    '''用递归的方法创建决策树，递归结束有两个条件：
    1、所有特征已用完 2、分支下的所有实例都被正确分类
    满足任意一个条件即结束递归'''
    classList=[example[-1] for example in dataSet]
    if classList.count(classList[0])==len(classList):#如果类别完全相同，则停止划分，返回当前类别
        return classList[0]
    if len(dataSet[0])==1:#如果已遍历完所有特征，则返回出现次数最多的类别
        return majorityCnt(classList)
    bestFeat=chooseBestFeatureToSplit(dataSet)
    bestFeatLabel=labels[bestFeat]
    myTree={bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues=[example[bestFeat] for example in dataSet]
    uniqueVals=set(featValues)
    for value in uniqueVals:
        subLabels=labels[:]
#         subLabels=labels[:bestFeat].extend(labels[bestFeat+1:])
        myTree[bestFeatLabel][value]=createTree(splitData(dataSet,bestFeat,value),subLabels)
    return myTree



























