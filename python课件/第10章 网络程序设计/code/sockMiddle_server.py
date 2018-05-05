import sys
import socket
import threading

#回复消息，原样返回
def replyMessage(conn):
    while True:
        data = conn.recv(1024)
        conn.send(data)
        if data.decode().lower() == 'bye':
            break
    conn.close()

def main():
    sockScr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockScr.bind(('', port))
    sockScr.listen(200)
    while True:
        try:
            conn, addr = sockScr.accept()
            #只允许特定主机访问本服务器
            if addr[0] != onlyYou:
                conn.close()
                continue
            #创建并启动线程
            t = threading.Thread(target=replyMessage, args=(conn,))
            t.start()        
        except:
            print('error')

if __name__ == '__main__':
    try:
        #获取命令行参数
        port = int(sys.argv[1])
        onlyYou = sys.argv[2]
        main()
    except:
        print('Must give me a number as port')
        
