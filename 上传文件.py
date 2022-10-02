'''-----------------------------------------功能函数------------------------------------------------'''
def replace(abcd):
    dcba=abcd.replace('/','\\')
    return dcba
'''----------------------------------------建立文件-------------------------------------------------'''
def mkdir(path):
    # 引入模块
    import os

    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path) 

        print(path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+' 目录已存在')
        return False

import time
import os
#变为编辑模式
garder = os.path.dirname(os.path.realpath(__file__))
Y=str(time.strftime("%Y", time.localtime()))
wY=garder+'\\文件\\'+Y
mkdir(wY)
#建立年
garder = os.path.dirname(os.path.realpath(__file__))
m=str(time.strftime("%m", time.localtime()))
wm=garder+'\文件\\''\\'+Y+'\\'+m
mkdir(wm)
#建立月
garder = os.path.dirname(os.path.realpath(__file__))
d=str(time.strftime("%d", time.localtime()))
wd=garder+'\文件\\'+'\\'+Y+'\\'+'\\'+m+'\\'+d
mkdir(wd)
#建立日
'''--------------------------------------------选文件-------------------------------------------------------------'''
import tkinter as tk
from tkinter import filedialog
root=tk.Tk()
root.withdraw()
ask=input('文件还是文件夹(0/1):\n')
if ask=='0':
    filename=filedialog.askopenfilename()
else:
    filename=filedialog.askdirectory()
'''-------------------------------------------复制------------------------------------------------------------------'''
if ask=='0':
    import os
    os.popen('copy '+replace(filename)+' '+wd)
else:
    import shutil
    name=input('文件夹名：\n')
    print('有点大稍等一下！(^__^)')
    shutil.copytree(replace(filename),wd+'\\'+name)
print('在你的下载网址后加上以访问')
print('/'+Y+'/'+m+'/'+d+'/<文件名>')
input('回车关闭...')

