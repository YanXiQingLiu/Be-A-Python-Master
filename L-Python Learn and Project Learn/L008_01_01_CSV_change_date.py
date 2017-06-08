#重新格式化数据并写入到CSV文件

import csv 

#datetime模块中导入datetime类
from datetime import datetime     


#创建一个函数来转换日期
def convertDate(item):
    #提取日期域
    theDate = item[-1]
    #使用datetime.strptime()解析日期域
    dateObj = datetime.strptime(theDate,'%Y-%m-%d')
    #使用datetime.strftime()涵数通过重新排列域并使用斜线/作为分隔符。
    dateStr = datetime.strftime(dateObj,'%m/%d/%Y')
    #重新赋值
    item[-1] = dateStr
    return item

with open('tooldesc.csv') as td:
    rdr = csv.reader(td)
    items = list(rdr)

items = [convertDate(item) for item in items]

with open('tooldesc2.csv', 'w', newline='') as td:
    wrt = csv.writer(td)
    for item in items:
        wrt.writerow(item)
