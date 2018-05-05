import win32con
import win32api
import os

def del_dir(path):
    for file in os.listdir(path):
        file_or_dir = os.path.join(path,file)
        if os.path.isdir(file_or_dir) and not os.path.islink(file_or_dir):
            del_dir(file_or_dir) #递归删除子文件夹及其文件
        else:
            try:
                os.remove(file_or_dir) #尝试删除该文件，
            except:#无法删除，很可能是文件拥有特殊属性
                win32api.SetFileAttributes(file_or_dir, win32con.FILE_ATTRIBUTE_NORMAL)
                os.remove(file_or_dir) #修改文件属性，设置为普通文件，再次删除
    os.rmdir(path) #delete the directory here
del_dir("E:\\old")
