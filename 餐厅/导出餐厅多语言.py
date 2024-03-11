import xml.etree.ElementTree as ET

dir_path = '/Volumes/T7/cook/cook-client-sunshine-dev/Assets/ChefMenu/Resources/Configs/Locales'
language = ['english','korean','French','German','Japanese','Russian','Portuguese','Spanish','Italian','Chinese(Traditional)','Chinese(Simplified)','Vietnamese','Turkish']
language = ['English','Korean','French','German','Japanese','Russian','Portuguese','Spanish','Italian','ChineseTraditional','ChineseSimplified']

key = []
lang_data = {}

# 定义递归函数遍历节点
def traverse_xml(element, parent_tag, first, array):
    tag = element.tag if parent_tag == '' else parent_tag + '/' + element.tag 
    if len(element) == 0 and first:
        text = element.attrib['text']
        print(f'{tag}: {text}')
        key.append(tag)
        array.append(text)

    # 遍历子节点
    for child in element:
        traverse_xml(child, tag, first, array)

for i in range(0, len(language)):  # 迭代1到5的整数
    lang = language[i]
    file = f'{dir_path}/Config_Locale_{lang}.xml'
    tree = ET.parse(file)
    root = tree.getroot()
    # 调用递归函数遍历根节点的子节点
    lang_data[lang] = [] 
    for child in root:
        traverse_xml(child, '', i == 0, lang_data[lang])
    
    break
