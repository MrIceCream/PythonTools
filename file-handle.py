# -*- coding: utf-8 -*-
'''
@author: yzk
@support: 835627891@qq.com
'''

import os
from hashlib import md5
import shutil

def get_fullpath_by_extension(rootdir, extensions=None):
    ''' 获取路径下的所有文件 根据extensions '''
    __re = []
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            fullpath = os.path.join(parent, filename)
            path_extension=os.path.splitext(fullpath)[1]
            if (extensions and path_extension in extensions) or not extensions:
                result = fullpath.replace("\\", "/")
                __re.append(result)
    return __re



def md5_file(path):
    '''md5 hash'''
    with open(path, "rb") as f:
        m=md5()
        m.update(f.read())
        return m.hexdigest()



def copy_to(file_list, target):
    """
    单层文件拷贝
    """
    for file_path in file_list:
        shutil.copy(file_path, target)



def copy_dir(source, target, extensions=None):
    """
    删除target的资源 将source覆盖
    """
    li = get_fullpath_by_extension(source, extensions)
    if os.path.exists(target):
        shutil.rmtree(target)
    time.sleep(1)
    for full_path in li:
        full_path = full_path.replace("\\", "/")
        if "/temp/" in full_path or "/.svn/" in full_path:
            continue
        pure_path = os.path.relpath(full_path, source)
        target_path = os.path.join(target, pure_path)

        target_dir = os.path.split(target_path)[0]

        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        shutil.copyfile(full_path, target_path)


if __name__ == '__main__':
    print md5_file('README.md')