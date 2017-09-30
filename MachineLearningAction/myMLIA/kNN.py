# -*- coding: utf-8 -*-.
'''
Created on Sep 17, 2017
kNN: k Nearest Neighbors

Input:      inX: vector to compare to existing dataset (1xN)
            dataSet: size m data set of known vectors (NxM)
            labels: data set labels (1xM vector)
            k: number of neighbors to use for comparison (should be an odd number)

Output:     the most popular class label

@author: yujingbaobao
'''
from numpy import *
import operator
def createDataSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=['A','A','B','B']
    return group,labels

def classify0(inX,dataSet,labels,k):
    '''
    :param inX:测试样本的特征 
    :param dataSet: 训练样本集
    :param labels: 训练样本的标签集
    :param k: 
    :return: 测试样本所属的标签（labels中的一个）
    '''
    #距离计算
    dataSetSize=dataSet.shape[0]
    diffMat=tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat=diffMat**2
    sqDistances=sqDiffMat.sum(axis=1)
    distances=sqDistances**0.5
    #选择距离最小的K个样本，并按类统计
    sortedDistIndicies=distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel=labels[sortedDistIndicies[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
    sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def file2matrix(filename):
    '''
    :param filename: 
    :return:returnMat：样本的特征  classLabelVector：样本的标签 
    '''
    fr=open(filename)
    arrayOLines=fr.readlines()
    numberOfLines=len(arrayOLines)
    returnMat=zeros((numberOfLines,3))
    classLabelVector=[]
    index=0
    for line in arrayOLines:
        line=line.strip()#截掉回车字符
        listFromLine=line.split('\t')
        returnMat[index,:]=listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index+=1
    return returnMat,classLabelVector

def autoNorm(dataSet):
    minVals=dataSet.min(0)
    maxVals=dataSet.max(0)
    ranges=maxVals-minVals
    normDataSet=zeros(shape(dataSet))
    m=dataSet.shape[0]
    normDataSet=dataSet-tile(minVals,(m,1))#tile将minVals从1*3复制成m*3的矩阵
    normDataSet=normDataSet/tile(ranges,(m,1))
    return normDataSet,ranges,minVals

def datingClassTest():
    hoRatio=0.1
    datingDataMat,datingLabels=file2matrix('datingTestSet2.txt')
    normMat,ranges,minVals=autoNorm(datingDataMat)
    m=normMat.shape[0]
    numTestVecs=int(m*hoRatio)
    errorCount=0.0
    for i in range(numTestVecs):
        classifierResult=classify0(normMat[i,:],
                                   normMat[numTestVecs:m,:],
                                   datingLabels[numTestVecs:m],
                                   3)
        print "the classifier came back with :%d, the real answer is %d"%(classifierResult,datingLabels[i])
        if (classifierResult!=datingLabels[i]):errorCount+=1.0
    print 'the total error rate is :%f'%(errorCount/float(numTestVecs))

def classifyPerson():
    resultList=['not at all','in small doses','in large doses']
    percentTats=float(raw_input('percentage of time spent playing video games?'))
    ffMiles=float(raw_input('frequent flier miles earned per year?'))
    iceCream=float(raw_input('liters of ice cream consumed per year?'))
    datingDataMat,datingLabels=file2matrix('datingTestSet2.txt')
    normMat,ranges,minVals=autoNorm(datingDataMat)
    inArr=array([ffMiles,percentTats,iceCream])
    classifierResult=classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
    print 'You will probably like this person:',resultList[classifierResult-1]

def img2vector(filename):
    returnVect=zeros((1,1024))
    fr=open(filename)
    for i in range(32):
        lineStr=fr.readline()
        for j in range(32):
            returnVect[0,32*i+j]=int(lineStr[j])
    return returnVect

from os import listdir
def handwritingClassTest():
    hwLabels=[]
    trainingFileList=listdir('./trainingDigits')#list可以列出目录里的内容
    m=len(trainingFileList)
    trainingMat=zeros((m,1024))
    for i in range(m):
        fileNameStr=trainingFileList[i]
        fileStr=fileNameStr.split('.')[0]
        classNumStr=int(fileNameStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:]=img2vector('trainingDigits/'+fileNameStr)
    testFileList=listdir('testDigits')
    errorCount=0.0
    mTest=len(testFileList)
    for i in range(mTest):
        fileNameStr=testFileList[i]
        fileStr=fileNameStr.split('.')[0]
        classNumStr=int(fileNameStr.split('_')[0])
        vectorUnderTest=img2vector('testDigits/'+fileNameStr)
        classifierResult=classify0(vectorUnderTest,trainingMat,hwLabels,1)#实验发现k越小，error rate越小
        print '%s:the classifier came back with:%d,the real answer is:%d'%(fileNameStr,classifierResult,classNumStr)
        if(classifierResult!=classNumStr):
            errorCount+=1.0
    print 'total error count:%s'%errorCount
    print 'error rate:%f'%(errorCount/float(mTest))




