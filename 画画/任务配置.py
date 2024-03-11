import json
from openpyxl import Workbook

json_path = '/Volumes/T7/sunshinegallery/sunshinegallery-client/Assets/Gallery/Bundles/Defs.pack/Defs/InApps.json'

# 打开JSON文件
with open(json_path) as file:
    # 加载JSON数据
    data = json.load(file)


# 创建工作簿和工作表
workbook = Workbook()
sheet = workbook.active
header = ['Id', 'Type', 'Sku.Android', 'Sku.Ios', 'Sku.Amazon', 'Cost']
sheet.append(header)

# 写入数据
for item in data['Products']:
    row = [item["Id"], item["Type"], item["Sku"]["Android"][0], item["Sku"]["Ios"][0], item["Sku"]["Amazon"][0], item["Cost"]]
    sheet.append(row)

# 保存工作簿
workbook.save('商品配置.xlsx')