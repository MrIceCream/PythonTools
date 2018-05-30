# -*- coding: utf-8 -*-
'''
@author: yzk
@support: 835627891@qq.com
'''

import xlrd
import types
from xlwt import *

# 读取excel文件

try:
    data = xlrd.open_workbook('lang.xlsx')

except BaseException, e:
    print ('格式错误，请保存一次文件!!!')
    exit(1)

# 获取工作表
table = data.sheets()[0]

# 行数
nrows = table.nrows

# 处理行数据
table_data = []
table_data.append(table.row_values(0))

for i in range(1, nrows):
    row_data = table.row_values(i)
    row_data_list = []
    max_len = 0
    min_len = 20

    for i in range(len(row_data)):
        row_data_list.append(row_data[i])
        if i > 0 :
		        min_len = min_len if len(row_data[i]) > min_len else len(row_data[i])
		        max_len = max_len if len(row_data[i]) < max_len else len(row_data[i])

    if min_len == max_len:
				continue

    for i in range(1, len(row_data_list)):
    		if min_len < len(row_data_list[i]) < max_len:
    				row_data_list[i] = '-'

    table_data.append(row_data_list)

# 创建结果表格
w = Workbook(encoding='utf-8')
ws = w.add_sheet('sheet1')

# # 初始化标题行
# ws.write(0, 0, u'行号')
# ws.write(0, 1, u'货号')
# ws.write(0, 2, u'品名')
# ws.write(0, 3, u'自编码')
# ws.write(0, 4, u'系统库存')
# ws.write(0, 5, u'实际数量')

# 遍历赋值
for i in range(len(table_data)):
    for j in range(len(table_data[i])):
        ws.write(i+1, j, table_data[i][j])

w.save('result.xls')