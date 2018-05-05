import socket
import sys
import re
import struct
import getpass

def main(serverIP):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((serverIP, 10600))
    userId = input('请输入用户名：')
    #使用getpass模块的getpass()方法获取密码，不回显
    userPwd = getpass.getpass('请输入密码：')
    message = userId+','+userPwd
    sock.send(message.encode())
    login = sock.recv(100)
    #验证是否登录成功
    if login == b'error':
        print('用户名或密码错误')
        return
    #整数编码大小
    intSize = struct.calcsize('I')
    while True:
        #接收客户端命令，其中##>是提示符
        command = input('##> ').lower().strip()
        #没有输入任何有效字符，提前进入下一次循环，等待用户继续输入
        if not command:
            continue
        #向服务端发送命令
        command = ' '.join(command.split())
        sock.send(command.encode())
        #退出
        if command in ('quit', 'q'):
            break
        #查看文件列表
        elif command in ('list', 'ls', 'dir'):
            loc_size = struct.unpack('I', sock.recv(intSize))[0]
            files = eval(sock.recv(loc_size).decode())
            for item in files:
                print(item)
        #切换至上一级目录
        elif ''.join(command.split()) == 'cd..':
            print(sock.recv(100).decode())
        #查看当前工作目录
        elif command in ('cwd', 'cd'):
            print(sock.recv(1024).decode())
        #切换至子文件夹
        elif command.startswith('cd '):
            print(sock.recv(100).decode())
        #从服务器下载文件
        elif command.startswith('get '):
            isFileExist = sock.recv(20)
            #文件不存在
            if isFileExist != b'ok':
                print('error')
            #文件存在，开始下载
            else:
                print('downloading.', end='')
                fp = open(command.split()[1], 'wb')
                while True:
                    print('.', end='')
                    data = sock.recv(4096)
                    if data == b'overxxxx':
                        break
                    fp.write(data)
                    sock.send(b'ok')
                fp.close()
                print('ok')
                
        #无效命令
        else:
            print('无效命令')
    sock.close()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:{0} serverIPAddress'.format(sys.argv[0]))
        exit()
    serverIP = sys.argv[1]
    if re.match(r'^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$', serverIP):
        main(serverIP)
    else:
        print('服务器地址不合法')
        exit()
