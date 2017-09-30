#-*-coding:utf-8-*-
import kNN
print 'kNN数值分类举例：'


group,labels=kNN.createDataSet()
print group,labels
print kNN.classify0([0,0],group,labels,3)

datingDataMat,datingLabels=kNN.file2matrix('datingTestSet2.txt')
print datingLabels[0:20]
from numpy import *
import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_subplot(111)
# ax.scatter(datingDataMat[:,1],datingDataMat[:,2])#显示第2列和第3列，同一个颜色
# plt.show()
# ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 15.0*array(datingLabels), 15.0*array(datingLabels))#显示第2列和第3列，不同的颜色
# plt.show()
# ax.scatter(datingDataMat[:,0], datingDataMat[:,1], 15.0*array(datingLabels), 15.0*array(datingLabels))#显示第1列和第2列，不同的颜色
# plt.show()

normMat,ranges,minVals=kNN.autoNorm(datingDataMat)
print normMat,ranges,minVals

print 'test error rate:'
kNN.datingClassTest()

print 'we made an predictor:'
kNN.classifyPerson()

