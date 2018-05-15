def defaultpar(a=5):
    print(a)
    print('=============')
defaultpar()

def keypar(a, b, c):
    '''关键参数demo'''
    print(a,b,c)
    print('=============')
keypar(c = 9, b = 8, a = 7)

def lengthchangeablepar(*a,**b):
    '''可变长度参数demo'''
    # a为元组
    for i in a:
        print(i)
    #b为字典
    for j in b.items():
        print('key=',j.key())
        print('valus=',j.valus())
    print('=============')
lengthchangeablepar(1,2,3,'i=1','j=2')

def iterunpack(a,b):
    #参数传递时的序列解包
    print(a+b)
    print('=============')
dict = {'i':1,'j':9}
iterunpack(*dict.values())