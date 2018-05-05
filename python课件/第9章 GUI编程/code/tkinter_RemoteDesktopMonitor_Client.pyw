import socket
import struct
from time import sleep
from PIL import ImageGrab

while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #假设监控端主机IP地址为192.168.0.103，并监听10600端口
        sock.connect(('192.168.0.103', 10600))
        #本地全屏幕截图
        im = ImageGrab.grab()
        size = im.size
        #发本地截图转换为字节串进行发送
        imageBytes = im.tobytes()
        #发送字节串总长度和图像大小
        fhead=struct.pack('I128sI',len(imageBytes),str(size).encode(),len(str(size).encode()))
        sock.send(fhead)
        rest = len(imageBytes)
        bufferSize = 1024*10
        while True:
            if rest > bufferSize:
                temp = imageBytes[:bufferSize]
                imageBytes = imageBytes[bufferSize:]
            else:
                temp = imageBytes[:]
            sock.send(temp)
            rest = rest - len(temp)            
            #本次截图发送完成
            if rest == 0:
                if sock.recv(100) == b'ok':
                    print('ok')
                    break
        sock.close()
    except:
        print('无法连接监控端')
