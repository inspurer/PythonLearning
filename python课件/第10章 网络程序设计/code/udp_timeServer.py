import socket
from datetime import datetime

#使用IPV4协议，使用UDP协议传输数据
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#绑定端口和端口号，空字符串表示本机任何可用IP地址
s.bind(('', 5005))
while True:
    data, addr=s.recvfrom(1024)
    #显示接收到的内容
    print('received message:{0} from {1}'.format(data.decode(),addr ))
    now = str(datetime.now())[:19]
    s.sendto(now.encode(), addr)
s.close( )
