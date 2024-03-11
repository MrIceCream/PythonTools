import json
import gzip
import requests

version = '0.2.0'

def request_json():
    # url = 'http://resource.doule.game/sunshinegallery/android/bundles/{0}/gallery_bundles/manifest.json'.format(version)
    url = 'https://resource.sunshinegallery.net/android/bundles/{0}/gallery_bundles/manifest.json'.format(version)
    response = requests.get(url)

    if response.status_code == 200:
        data = gzip.decompress(response.content).decode('utf-8')
        data = json.loads(data)
        # 将 JSON 数据写入新文件  
        with open('{0}_unzip.json'.format(version), 'w') as outfile:  
            json.dump(data, outfile, indent=4)
    else:
        print('请求失败，状态码：', response.status_code)

def ungzip():
    # 打开 gzip 文件  
    with gzip.open('{0}.json'.format(version), 'rt') as f:  
        # 解压并读取 JSON 数据  
        data = json.load(f)  
    
    # 将 JSON 数据写入新文件  
    with open('{0}_unzip.json'.format(version), 'w') as outfile:  
        json.dump(data, outfile, indent=4)

def zip():
    # 读取JSON文件
    with open('{0}_unzip.json'.format(version), 'r') as file:
        data = json.load(file)

    # 压缩并写入gzip文件
    with gzip.open('{0}.json.gz'.format(version), 'wb') as file:
        file.write(json.dumps(data).encode('utf-8'))

# 执行主函数
if __name__ == '__main__':
    # ungzip()
    # zip()
    request_json()