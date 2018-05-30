# -*- coding: utf-8 -*-
'''
@author: yzk
@support: 835627891@qq.com
'''

import os

def svn_lock(path):
    """
    锁定已修改svn文件
    """
    cmd = "svn status {path}".format(path=path)
    files = os.popen(cmd)
    for line in files:
        state = line[:1]
        if state == "M":
            dif_path = line[1:]
            dif_path = dif_path.strip()
            svn_command = 'svn lock -m "lock file" --force {path}'.format(path=dif_path)
            os.system(svn_command)
            # re = os.popen(svn_command)
            # print(re.read())



def svn_clean(path):
    """
    svn目录清理
    """
    svn_command = "svn cleanup {path}".format(path=path)
    os.system(svn_command)
    # re = os.popen(svn_command)
    # print(re.read())



def add_file(path):
    """
    自动添加本地不存在的文件到SVN
    """
    svn_command = "svn status {path}".format(path=path)
    result = os.popen(svn_command)
    for line in result:
        head = line[:1]
        if head == "?":
            add_path = line[1:]
            add_path = add_path.strip()
            add_command = "svn add {path}".format(path=add_path)
            os.system(add_command)
            # re = os.popen(add_command)
            # print(re.read())



def delete_file(path):
    """
    自动删除本地不存在的文件
    """
    svn_command = "svn status {path}".format(path=path)
    result = os.popen(svn_command)
    for line in result:
        head = line[:1]
        if head == "!":
            miss_path = line[1:]
            miss_path = miss_path.strip()
            del_command = "svn delete {path}".format(path=miss_path)
            os.system(del_command)
            # re = os.popen(del_command)
            # print(re.read())



def commit_file(path, log):
    """
    提交SVN
    """
    add_file(path)
    delete_file(path)
    svn_lock(path)
    svn_command = 'svn commit {path} -m "auto commit {log}"'.format(path=path, log=log)
    os.system(svn_command)
    # re = os.popen(svn_command)
    # print(re.read())



def update_svn(path):
    """
    更新SVN
    """
    svn_command="svn update {path}".format(path=path)
    os.system(svn_command)
    # re = os.popen(svn_command)
    # print(re.read())