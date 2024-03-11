import json
import gzip
import os
import shutil

# 读取JSON文件并解压缩
def read_gzip_json(file_path):
    # 打开gzip压缩的JSON文件
    with gzip.open(file_path, 'rt') as f:
        # 读取文件内容
        json_content = f.read()

    # 将JSON内容解析为Python对象
    data = json.loads(json_content)
    return data

# 遍历"Packs"数组并重命名文件
def rename_files(data, root_dir, hash_dir):
    packs = data["Packs"]
    for pack in packs:
        name = pack["Name"]
        hash_value = pack["Hash"]

        # 构建旧文件路径和新文件路径
        old_file_path = root_dir + name
        new_file_path = hash_dir + hash_value

        # 重命名文件
        shutil.copy2(old_file_path, new_file_path)
        print(f"Copy file: {old_file_path} -> {new_file_path}")

# 主函数
def main():
    # JSON文件路径
    root_dir = "/Users/mac/Desktop/docker/nginx/html/gallery/storage/0.1.0/"
    hash_dir = "/Users/mac/Desktop/docker/nginx/html/gallery/storage/bundles/0.1.0/"
    json_file_path = root_dir + "manifest.json"

    # 读取并解压缩JSON文件
    json_data = read_gzip_json(json_file_path)

    # 遍历并重命名文件
    rename_files(json_data, root_dir, hash_dir)


# 执行主函数
if __name__ == '__main__':
    main()