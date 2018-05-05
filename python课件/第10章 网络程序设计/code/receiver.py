import socket
#使用IPV4协议，使用UDP协议传输数据
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#绑定端口和端口号，空字符串表示本机任何可用IP地址
s.bind(('', 5000))
while True:
    data, addr=s.recvfrom(1024)
     #显示接收到的内容
    print('received message:{0} from PORT {1} on {2}'.format(data.decode(),
                                                             addr[1], addr[0]))
    if data.decode().lower() == 'bye':
        break
s.close( )
