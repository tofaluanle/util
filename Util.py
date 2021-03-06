# @auther 宋疆疆 
# @since 2017/9/12.
import os
import subprocess
import sys

import L


def execCmd(args, path=None):
    if path:
        L.d('Path: ' + path)
    else:
        L.d('Path: ' + os.getcwd())
    L.d('Exec: ' + ' '.join(args))

    if sys.platform == 'win32':
        shell = True
    else:
        shell = False

    if path:
        obj = subprocess.Popen(args, cwd=path, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1)
    else:
        obj = subprocess.Popen(args, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1)

    return obj


def execCmdWait(args, path=None, printOut=False):
    obj = execCmd(args, path)

    if printOut:
        if sys.platform == 'win32':
            encode = 'gbk'
        else:
            encode = 'utf-8'
        for line in obj.stdout:
            print(line.decode(encode).strip(), flush=True)
        for line in obj.stderr:
            print(line.decode(encode).strip(), flush=True)
    else:
        obj.stdout.readlines()

    obj.wait()
    return obj


def execCmdSimple(args, path=None, printOut=False):
    obj = execCmdWait(args, path, printOut)

    ret = obj.returncode
    if ret != 0:
        msg = 'Fail: ' + str(ret)
        raise Exception(msg)

    L.d('Success ')


def supplementSpace(s, tarLen, right=False):
    oriLen = len(s)
    for i in range(tarLen - oriLen):
        if right:
            s = s + ' '
        else:
            s = ' ' + s
    return s
