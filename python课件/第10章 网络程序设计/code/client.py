import socket

HOST = '127.0.0.1'          #服务端主机IP地址
PORT = 50007                #服务端主机端口号
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))     #连接连接
while True:
    c = input('Input the content you want to send:')
    s.sendall(c.encode())   #发送数据
    data = s.recv(1024)     #从客户端接收数据
    data = data.decode()
    print('Received:', data)
    if c.lower() == 'bye':
        break
s.close()                   #关闭连接
