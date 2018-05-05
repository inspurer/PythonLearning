import socket
import uuid

ip = socket.gethostbyname(socket.gethostname())
node = uuid.getnode()
macHex = uuid.UUID(int=node).hex[-12:]
mac = []
for i in range(len(macHex))[::2]:
    mac.append(macHex[i:i+2])
mac = ':'.join(mac)
print('IP:', ip)
print('MAC:', mac)
