import os
import sys
import zipfile                     #zipfile是标准库
try:
    from unrar import rarfile      #尝试导入扩展库，如果没有就临时安装
except:
    path = '"'+os.path.dirname(sys.executable)+'\\scripts\\pip" install --upgrade pip'
    os.system(path)
    path = '"'+os.path.dirname(sys.executable)+'\\scripts\\pip" install unrar'
    os.system(path)
    from unrar import rarfile    

def decryptRarZipFile(filename):
    if filename.endswith('.zip'):
        fp = zipfile.ZipFile(filename)
    elif filename.endswith('.rar'):
        fp = rarfile.RarFile(filename)
    desPath = filename[:-4]        #解压缩的目标文件夹
    if not os.path.exists(desPath):
        os.mkdir(desPath)
    try:                           #尝试不用密码解压缩
        fp.extractall(desPath)
        fp.close()
        print('No password')
        return
    except:                        #使用密码字典进行暴力破解
        try:
            fpPwd = open('pwddict.txt')
        except:
            print('No dict file pwddict.txt in current directory.')
            return
        for pwd in fpPwd:
            pwd = pwd.rstrip()
            try:
                if filename.endswith('.zip'):
                    for file in fp.namelist():
                        #因为zipfile的字符串编码问题，需要重新编码再解码，避免中文乱码
                        fp.extract(file, path=desPath, pwd=pwd.encode())
                        os.rename(desPath+'\\'+file,
                                  desPath+'\\'+file.encode('cp437').decode('gbk'))
                    print('Success! ====>'+pwd)
                    fp.close()
                    break
                elif filename.endswith('.rar'):
                    fp.extractall(path=desPath, pwd=pwd)
                    print('Success! ====>'+pwd)
                    fp.close()
                    break
            except:
                pass
        fpPwd.close()

if __name__ == '__main__':
    filename = sys.argv[1]
    if os.path.isfile(filename) and filename.endswith(('.zip', '.rar')):
        decryptRarZipFile(filename)
    else:
        print('Must be Rar or Zip file')
