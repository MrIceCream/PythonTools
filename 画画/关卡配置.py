import json
from openpyxl import Workbook

json_path = '/Volumes/T7/sunshinegallery/sunshinegallery-client/Assets/Gallery/Bundles/Defs.pack/Defs/StoryLevels.json'

# 打开JSON文件
with open(json_path) as file:
    # 加载JSON数据
    data = json.load(file)


# 创建工作簿和工作表
workbook = Workbook()
sheet = workbook.active

# 写入表头
header = list(data['Levels'][0].keys())
sheet.append(header)

# 写入数据
for item in data['Levels']:
    row = list(item.values())[:5]
    sheet.append(row)

# 保存工作簿
workbook.save('关卡配置.xlsx')