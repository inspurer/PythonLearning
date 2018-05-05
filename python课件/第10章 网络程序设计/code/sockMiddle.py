import sys
import socket
import threading

def middle(conn, addr):
    #面向服务器的Socket
    sockDst = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockDst.connect((ipServer,portServer))
    while True:
        data = conn.recv(1024).decode()
        print('收到客户端消息：'+data)
        if data == '不要发给服务器':
            conn.send('该消息已被代理服务器过滤'.encode())
            print('该消息已过滤')
        elif data.lower() == 'bye':
            print(str(addr)+'客户端关闭连接')
            break
        else:
            sockDst.send(data.encode())
            print('已转发服务器')
            data_fromServer = sockDst.recv(1024).decode()
            print('收到服务器回复的消息：'+data_fromServer)
            if data_fromServer == '不要发给客户端':
                conn.send('该消息已被代理服务器修改'.encode())
                print('消息已被篡改')
            else:
                conn.send(b'Server reply:'+data_fromServer.encode())
                print('已转发服务器消息给客户端')
        
    conn.close()
    sockDst.close()

def main():
    sockScr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockScr.bind(('', portScr))
    sockScr.listen(200)
    print('代理已启动')
    while True:
        try:
            conn, addr = sockScr.accept()
            t = threading.Thread(target=middle, args=(conn, addr))
            t.start()
            print('新客户：'+str(addr))
        except:
            pass
        
if __name__ == '__main__':
    try:
        #(本机IP地址,portScr)<==>(ipServer,portServer)
        #代理服务器监听端口
        portScr = int(sys.argv[1])
        #服务器IP地址与端口号
        ipServer = sys.argv[2]
        portServer = int(sys.argv[3])
        main()
    except:
        print('Sth error')
