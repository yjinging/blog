# -*- coding: utf-8 -*-.
import urllib2
import json
import re
from collections import namedtuple
from sys import argv

#readme：本脚本用于删除文件系统的volume
#SYNOPSIS：python fs_delete_volumes.py master-node-lookup-url volume-ids
#使用示例：python fs_delete_volumes.py http://192.168.0.1:9333/vol/lookup?volumeId= 1 2 3
url, ids = argv[1], argv[2:]
for id in ids:
    html = urllib2.urlopen(url + id)
    hjson = json.loads(html.read())
    try:
        for address in hjson[id]['locations']:
            response = urllib2.urlopen('http://' + address['url'] + '/admin/volume/delete?volume=' + id)
            print response.read()
    except:
        print 'volume %s not exist' % (id)
