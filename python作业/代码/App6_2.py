class Vector3D:
    i,j,k = 0.0,0.0,0.0
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
        print('新建的向量为:')
        self.printVector()
    def printVector(self):
        #str 2 float
        self.i = (float)("%.2f" % self.i)
        self.j = (float)("%.2f" % self.j)
        self.k = (float)("%.2f" % self.k)
        print(str(self.i)+'i+'+str(self.j)+'j+'+str(self.k)+'k')
    #add()和minus()都是原地操作
    def add(self,anotherVector):
        self.i += anotherVector.i
        self.j += anotherVector.j
        self.k += anotherVector.k
        print('相加后的向量为:')
        self.printVector()
    def minus(self,anotherVector):
        self.i -= anotherVector.i
        self.j -= anotherVector.j
        self.k -= anotherVector.k
        print('相减后的向量为:')
        self.printVector()
        #coefficient:系数
    def multiply(self,coefficient):
        self.i *= coefficient
        self.j *= coefficient
        self.k *= coefficient
        print('乘系数后的向量为:')
        self.printVector()
    def divide(self,coefficient):
        '''coefficient:系数,推荐使用浮点数'''
        self.i /= coefficient
        self.j /= coefficient
        self.k /= coefficient
        print('除系数后的向量为:')
        self.printVector()
        
    
