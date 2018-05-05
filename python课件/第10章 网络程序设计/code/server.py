import socket

words = {'how are you?':'Fine,thank you.',
         'how old are you?':'38',
         'what is your name?':'Dong FuGuo',
         "what's your name?":'Dong FuGuo',
         'where do you work?':'SDIBT',
         'bye':'Bye'}
HOST = ''
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#绑定socket
s.bind((HOST, PORT))
#开始监听
s.listen(1)
print('Listening at port:',PORT)
conn, addr = s.accept()
print('Connected by', addr)
while True:
    data = conn.recv(1024)
    data = data.decode()
    if not data:
        break
    print('Received message:', data)
    conn.sendall(words.get(data, 'Nothing').encode())
conn.close()
