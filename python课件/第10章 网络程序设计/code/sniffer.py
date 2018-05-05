import socket
import threading
import time

activeDegree = dict()
flag = 1
# the public network interface
def main():
    global activeDegree
    global flag
    HOST = socket.gethostbyname(socket.gethostname())
    # create a raw socket and bind it to the public interface
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    s.bind((HOST, 0))
    # Include IP headers
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    # receive all packages
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    # receive a package
    while True:
        if flag==0:
            break
        c = s.recvfrom(65565)
        host = c[1][0]
        activeDegree[host] = activeDegree.get(host, 0)+1
        if c[1][0]!='10.2.1.8':
            print(c)
    # disabled promiscuous mode
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
    s.close()
t = threading.Thread(target=main)
t.start()
#让线程运行60秒
time.sleep(60)
#结束线程
flag = 0
t.join()
for item in activeDegree.items():
    print(item)
