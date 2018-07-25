# ! /usr/bin/python
# -*- coding: utf-8 -*-

import chardet
import re, os
import json
import urllib
import sys
import random
import hashlib
import time


reload(sys)
sys.setdefaultencoding( "utf-8" )

# 调用baidu翻译api
def trans_baidu(src):
    if src == '':
        return src

    hl = hashlib.md5()
    ran = random.random()
    appid = 20180721000187581  # 百度开发者appid
    sign = bytes(appid) + src + bytes(ran) + "4Go5uJHoY2SuexGcXORb"
    hl.update(sign.encode(encoding='utf-8'))

    url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    params = {'q':src, 'from':'kor', 'to':'zh', 'appid':appid, 'salt':ran, 'sign':hl.hexdigest()}


    try:
        params = urllib.urlencode(params)
        ret = urllib.urlopen(url, params)
        ret_data = ret.read()

    except Exception, e:
        raise e
    else:
        decoded = json.loads(ret_data)
        dst = []
        for result in decoded["trans_result"]:
            dst.append(result["dst"])

        return '\n'.join(dst)


def google_translate(src):
    if src == '':
        return src

    from googletrans import Translator
    translator = Translator()
    translations = translator.translate(src.split('\n'), dest='zh-CN')

    result = []
    for translation in translations:
        # print(translation.origin, ' -> ', translation.text)
        result.append(translation.text)

    return '\n'.join(result)


def get_file_list(_dir, postfix=''):
    _file_list = []
    files = os.listdir(_dir)

    for item in files:
        if os.path.isfile(_dir + item):
            if item.endswith(postfix):
                _file_list.append(_dir + item)
        else:
            if os.path.isdir(_dir + item):
                _file_list.extend(get_file_list(_dir + item+'/', postfix))

    return _file_list

def replace_kor(content, reg):
    result = re.findall(reg, content.decode('utf-8'))
    result_str = '\n'.join(result)

    if len(result) == 0:
        return content

    trans_result_str = google_translate(result_str)
    trans_result = trans_result_str.split('\n')

    for i in range(0, len(trans_result)):
        # print result[i], trans_result[i]
        content = content.replace(result[i], trans_result[i], 1)

    return content


def convert(_file_list):
    for index,_file in enumerate(_file_list):
        print index * 1.0 /len(_file_list) 
        with open(_file, 'r') as fp:
            content = fp.read()

            code = chardet.detect(content)

            content = content.decode(code.get('encoding')).encode('utf-8')

        # 如果没有韩文，不写入文件
        if not re.findall(u"[\uac00-\ud7ff]", content.decode('utf-8')):
            continue
        
        print _file            
        content = replace_kor(content, u"[\uac00-\ud7ff][\uac00-\ud7ff\u0020]*[\uac00-\ud7ff]")
        content = replace_kor(content, u"[\uac00-\ud7ff]")

        with open(_file, 'w') as fp:
            fp.write(content)

        # time.sleep(0.1)

if __name__ == '__main__':
    path = os.getcwd() + '/'

    convert(get_file_list(path, '.cs'))



