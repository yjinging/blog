#-*-coding:utf-8-*-
import kNN

group,labels=kNN.createDataSet()
print group,labels
print kNN.classify0([0,0],group,labels,3)

datingDataMat,datingLabels=kNN.file2matrix('datingTestSet2.txt')
print datingLabels[0:20]
from numpy import *
import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_subplot(111)
# ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
# plt.show()
# ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15*(datingLabels),15*(datingLabels))
ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 15.0*array(datingLabels), 15.0*array(datingLabels))
plt.show()