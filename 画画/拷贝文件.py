import os
import shutil
import openpyxl
import re

def copy_spine():
    # 指定源目录和目标目录的路径，并调用函数拷贝并重命名目录
    source_directory = '/Volumes/各组打样存档/餐厅项目/角色/动作/{0}/输出文件/'  # 替换为源目录 A 的路径
    destination_directory = '/Volumes/T7/cook/cook-client-sunshine/Assets/ChefMenu/FlashTools/Kitchens/Common/Visitors_New/Char{0}/'  # 替换为目标目录 B 的路径
    
    for i in range(1, 23):
        padded_number = "{:02d}".format(i)
        source = source_directory.format(padded_number)
        destination = destination_directory.format(padded_number)
        
        if os.path.exists(source) == False:
            continue

        print(f"已拷贝目录 {source} 到 {destination}")
        # 获取源目录下所有文件列表
        file_list = os.listdir(source)

        # 遍历文件列表，逐个拷贝文件到目标目录
        for file_name in file_list:
            source_path = os.path.join(source, file_name)
            target_path = os.path.join(destination, file_name)
            shutil.copy2(source_path, target_path)


def replace_camel_case(string):
    pattern = re.compile(r'(?<=\w)([A-Z])')
    new_string = pattern.sub(r' \1', string)
    return new_string.replace(' ', '_')

fix_map = {
    "Preview_Cake__Wedding":"Preview_Wedding_Cake",
    "Preview_Couple_Watching_T_V":"Preview_Couple_Watching_TV",
    "Preview_Fox":"FoxPreview",
    "Preview_Leo":"LeoPreview",
    "Preview_Rats2020":"Preview_Rats_2020",
    "Preview_Retro_T_V":"Preview_Retro_TV",
    "Preview_Set__Wild__Animals":"Preview_Wild_Animals_Set",
    "Preview_Tea":"TeaPreview",
    "Preview_T_V_Evening":"Preview_TV_Evening",
    "Preview_U_F_O_Pattern":"Preview_UFO_Pattern",
    "Preview_Zoo":"ZooPreview",
}

def copy_preview_image():
    source_json_directory = '/Volumes/各组打样存档/画画二合/批处理生成关卡JSON/20231211(401-500)/export_json'  # 替换为源目录 A 的路径
    source_png_directory = '/Volumes/各组打样存档/画画二合/批处理生成关卡JSON/20231211(401-500)/preview/{0}.png'  # 替换为源目录 A 的路径
    destination_directory = '/Volumes/T7/sunshinegallery/sunshinegallery-client-new/Assets/Gallery/Bundles/Levels/{0}.pack/Preview_{1}.png'  # 替换为目标目录 B 的路径
    
    json_files = [f for f in os.listdir(source_json_directory) if f.endswith(".json")]
    result_dict = {}

    for file in json_files:
        file_name = os.path.splitext(file)[0]
        key = file_name
        vlue = "Preview_{0}".format(replace_camel_case(file_name))
        result_dict[key] = value

    for key, value in result_dict.items():
        source_file = source_png_directory.format(value)
        destination_file = destination_directory.format(key, replace_camel_case(key))

        if os.path.exists(source_file) and os.path.exists(destination_file):
            shutil.copy2(source_file, destination_file)
            # print('{0} =====> {1}'.format(source_file, destination_file))
        else:
            for k, v in fix_map.items():
                if value == k:
                    source_file = source_file.replace(k, v)
                    destination_file = destination_file.replace(k, v)
                    break
            
            if os.path.exists(source_file) and os.path.exists(destination_file):
                shutil.copy2(source_file, destination_file)
            else:
                print('{0}文件不存在'.format(source_file))

def copy_fbx():
    source_file = '/Users/mac/Downloads/2023_08_11/{0}.fbx'
    preview_source_file = '/Users/mac/Downloads/2023_08_11/Preview_{0}.png'

    destination_file = '/Volumes/T7/sunshinegallery/sunshinegallery-client/Assets/2023_08_11'
    preview_destination_file = '/Volumes/T7/sunshinegallery/sunshinegallery-client/Assets/Gallery/Bundles/Levels/{0}.pack/Preview_{1}.png'  # 替换为目标目录 B 的路径
    
    levels = ['Butterfly','FlowersHairGirl','Parrots','Balloon','Love','Clouds','RedPanda','Mandala','Salome','Deer']
    
    os.makedirs(destination_file, exist_ok=True)
    for level in levels:
        shutil.copy2(source_file.format(level), destination_file)
        shutil.copy2(preview_source_file.format(replace_camel_case(level)), 
                     preview_destination_file.format(level, replace_camel_case(level)))

def copy_all_fbx():
    source_dir = '/Users/mac/Downloads/2023_08_11/'
    preview_source_file = '/Users/mac/Downloads/2023_08_11/Preview_{0}.png'

    destination_dir = '/Volumes/T7/sunshinegallery/sunshinegallery-client/Assets/FBX_IMPORT/'
    preview_destination_file = '/Volumes/T7/sunshinegallery/sunshinegallery-client/Assets/Gallery/Bundles/Levels/{0}.pack/Preview_{1}.png'  # 替换为目标目录 B 的路径
    
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".fbx"):
                source_file = os.path.join(root, file)
                destination_file = os.path.join(destination_dir, file)
                shutil.copy2(source_file, destination_file)
                
                level = file.replace('.fbx','')
                preview = replace_camel_case(level)
                if os.path.exists(preview_source_file.format(preview)):
                    shutil.copy2(preview_source_file.format(preview), preview_destination_file.format(level, preview))
                else:
                    print('预览图不存在: {0}'.format(preview))

copy_preview_image()
# copy_fbx()
# copy_all_fbx()