import socket
import sys

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(sys.argv[1].encode() , ("192.168.0.103" ,5000))#假设192.168.0.103是接收端机器的IP地址
s.close( )
