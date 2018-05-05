import struct
n = 1300000000
x = 96.45
b = True
s = 'a1@中国'
sn = struct.pack('if?', n, x, b)
f = open('sample_struct.dat', 'wb')
f.write(sn)
f.write(s.encode())
f.close()
