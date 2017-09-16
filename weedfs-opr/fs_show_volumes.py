# -*- coding: utf-8 -*-.
import urllib2
import json
import re
from collections import namedtuple
from sys import argv

#readme：本脚本用于显示文件系统的所有volume
#SYNOPSIS：python fs_show_volumes.py master-node-status-url
#使用示例：python fs_show_volumes.py http://192.168.0.1:9333/vol/status
url=argv[1]
print argv
html=urllib2.urlopen(url)
hjson=json.loads(html.read())

list=[]
val=namedtuple('val','id collection size filecount')
def comp(val1,val2):
    if val1.id>val2.id:
        return 1
    elif val1.id<val2.id:
        return -1
    else:
        return 0

for dc in hjson['Volumes']['DataCenters']:
    # print dc
    for r in hjson['Volumes']['DataCenters'][dc]:
        # print r
        for ip_endpoint in hjson['Volumes']['DataCenters'][dc][r]:
            # print ip_endpoint
            for item in  hjson['Volumes']['DataCenters'][dc][r][ip_endpoint]:
                collection=item['Collection']
                if re.match('DATA_.*_[0-9]{6}',collection):
                    # print item['Id'],collection,int(item['Size']/1024/1024/1024),item['FileCount']#size -> G id:sort
                    id,collection,size,fileCount=int(item['Id']),collection,item['Size']/1024.0/1024/1024,item['FileCount']
                    list.append(val(id,collection,size,fileCount))
                    # print id, collection, size, fileCount


list.sort(comp)
for i in list:
    print i#todo：最好把print的内容的val()去掉，并把size改为只保留两位小数







