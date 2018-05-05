import socket
from os.path import commonprefix

words = {'how are you?':'Fine,thank you.',
         'how old are you?':'38',
         'what is your name?':'Dong FuGuo',
         "what's your name?":'Dong FuGuo',
         'where do you work?':'University',
         'bye':'Bye'}
HOST = ''
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#绑定socket
s.bind((HOST, PORT))
#开始监听一个客户端连接
s.listen(1)
print('Listening on port:',PORT)
conn, addr = s.accept()
print('Connected by', addr)
#开始聊天
while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print('Received message:', data)
    #尽量猜测对方要表达的真正意思
    m = 0
    key = ''
    for k in words.keys():
        #删除多余的空白字符
        data = ' '.join(data.split())
        #与某个“键”非常接近
        #就直接返回
        if len(commonprefix([k, data])) > len(k)*0.7:
            key = k
            break
        #使用选择法
        #选择一个重合度较高的“键”
        length = len(set(data.split())&set(k.split()))
        if length > m:
            m = length
            key = k
    #选择合适的信息进行回复
    conn.sendall(words.get(key, 'Sorry.').encode())
conn.close()
s.close()
