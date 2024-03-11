from openpyxl import Workbook
from jsoncomment import JsonComment
import os

folder_path = '/Volumes/T7/sunshinegallery/sunshinegallery-client/Assets/Gallery/Bundles/Levels'  # 目录路径
file_dict = {}

for folder_name in os.listdir(folder_path):
    folder_dir = os.path.join(folder_path, folder_name)

    folder_name = folder_name.replace('.pack', '')
    if folder_name == 'Flowersboat':
        folder_name = 'FlowersBoat'
    if os.path.isdir(folder_dir):
        for file_name in os.listdir(folder_dir):
            file_path = os.path.join(folder_dir, file_name)
            file_basename = os.path.splitext(file_name)[0]
            if file_name.endswith('.prefab'):
                if folder_name in file_dict:
                    file_dict[folder_name]['prefab'] = file_basename
                else:
                    file_dict[folder_name] = {'prefab': file_basename}
            elif file_name.endswith('.png'):
                if folder_name in file_dict:
                    file_dict[folder_name]['png'] = file_basename
                else:
                    file_dict[folder_name] = {'png': file_basename}

print(len(file_dict))

jc = JsonComment()
def_path = '/Volumes/T7/sunshinegallery/sunshinegallery-client/Assets/Gallery/Bundles/Defs.pack/Defs/'

# 创建工作簿和工作表
workbook = Workbook()
sheet = workbook.active

# 写入表头
header = ["Id","Name","Image","Preview"]
sheet.append(header)

all_level = []

json_path = def_path + 'StoryLevels.json'
# 打开JSON文件
with open(json_path) as file:
    # 加载JSON数据
    data = jc.load(file)
# 写入数据
for item in data['Levels']:
    row = list(item.values())[:4]
    row[1] = ''
    all_level.append(row)


json_path = def_path + 'StoryLevelsSkip.json'
# 打开JSON文件
with open(json_path) as file:
    # 加载JSON数据
    data = jc.load(file)
# 写入数据
for item in data['Levels']:
    row = list(item.values())[:4]
    row[1] = ''
    all_level.append(row)


json_path = def_path + 'Level_Rewardeds.json'
# 打开JSON文件
with open(json_path) as file:
    # 加载JSON数据
    data = jc.load(file)
# 写入数据
for categorie in data['Categories']:
    for item in categorie['Levels']:
        row = list(item.values())[:4]
        all_level.append(row)


json_path = def_path + 'LevelPacks.json'
# 打开JSON文件
with open(json_path) as file:
    # 加载JSON数据
    data = jc.load(file)
# 写入数据
for categorie in data['Packs']:
    for item in categorie['Levels']:
        row = list(item.values())[:4]
        all_level.append(row)


json_path = def_path + 'LevelStrips.json'
# 打开JSON文件
with open(json_path) as file:
    # 加载JSON数据
    data = jc.load(file)
# 写入数据
for categorie in data['Strips']:
    for item in categorie['Levels']:
        row = list(item.values())[:4]
        all_level.append(row)


json_path = def_path + 'MultiLevelPacks.json'
# 打开JSON文件
with open(json_path) as file:
    # 加载JSON数据
    data = jc.load(file)
# 写入数据
for categorie in data['Packs']:
    for part in categorie['Parts']:
        for item in part['Levels']:
            row = list(item.values())[:4]
            all_level.append(row)


json_path = def_path + 'Events.json'
# 打开JSON文件
with open(json_path) as file:
    # 加载JSON数据
    data = jc.load(file)
# 写入数据
for categorie in data['Events']:
    if 'Event' not in categorie:
        continue
    if 'Episodes' not in categorie['Event']:
        continue
    for part in categorie['Event']['Episodes']:
        row = list(part['Level'].values())[:4]
        all_level.append(row)


for level in all_level:
    prefab = level[2]
    if prefab in file_dict:
        del file_dict[prefab]
    else:
        print('key不存在: {0}'.format(prefab))

for key in file_dict:
    all_level.append([file_dict[key]['prefab'],'',file_dict[key]['prefab'],file_dict[key]['png']])

for level in all_level:
    sheet.append(level)
# 保存工作簿
workbook.save('所有关卡配置.xlsx')