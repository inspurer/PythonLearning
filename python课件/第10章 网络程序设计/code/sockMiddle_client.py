import sys
import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    while True:
        data = input('What do you want to ask:')
        sock.send(data.encode())
        print(sock.recv(1024).decode())
        if data.lower() == 'bye':
            break
    sock.close()

if __name__ == '__main__':
    try:
        #代理服务器的IP地址和端口号
        ip = sys.argv[1]
        port = int(sys.argv[2])
        main()
    except:
        print('Sth error')
