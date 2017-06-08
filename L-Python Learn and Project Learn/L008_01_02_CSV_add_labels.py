#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：Xuhong Wen
# 将标题行添加到CSV文件
import csv

fields = ['ItemID', 'Name', 'Description', 'Owner',
          'Price', 'Condition', 'DateRegistered']

# 打开原始文件tooldesc2.csv，用DictReader将它读入到列表items中，-
# 并使用fields列表作为DictReader的fieldnames参数来初始化它。
with open('C:\\Python36\\ToolhireData\\tooldesc2.csv') as td_in:
    rdr = csv.DictReader(td_in, fieldnames=fields)
    items = [item for item in rdr]

# （在绝对路径C:\\Python36\\ToolhireData\\中）-
#   创建tooldesc3.csv文件并写入标题和items列表
with open('C:\\Python36\\ToolhireData\\tooldesc3-5.csv', 'w', newline='') as td_out:
    wrt = csv.DictWriter(td_out, fieldnames=fields)
    #写入标题行
    wrt.writeheader()
    #写入items列表
    wrt.writerows(items)
