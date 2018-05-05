import socket
import time

while True:
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto('ask for time'.encode() , ("10.2.1.2" ,5005))
    data, addr=s.recvfrom(1024)
    print(data.decode())
    s.close( )
    time.sleep(1)
