from PIL import Image
import os

source_dir = "/Volumes/T7/cook/cook-client-sunshine/Assets/GameResources/UI/Cook_Avatars"
replace_image_path = "gray.png"
new_size = (112, 112)

# 遍历目录中的所有文件
for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)
    
    # 检查是否为图片文件
    if os.path.isfile(file_path) and filename.lower().endswith(('.png')):
        # 打开图片
        image = Image.open(file_path)
        
        # 检查图片尺寸
        if image.size != new_size:
            # 替换图片
            replace_image = Image.open(replace_image_path)
            replace_image.save(file_path)
            print(f"替换图片: {filename}")
        
        # 关闭图片
        image.close()