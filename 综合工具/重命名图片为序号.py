import glob
import os

# 获取a目录下的所有图片文件
img_files = glob.glob('/Users/mac/Downloads/1/*.jpg')

# 遍历图片文件
for i, img_file in enumerate(img_files):
    # 使用enumerate函数获取图片的序号
    num = i + 1
    # 生成新的文件名
    new_name = f'/Users/mac/Downloads/1/{num}.jpg'
    # 使用os.rename()函数重命名图片
    os.rename(img_file, new_name)