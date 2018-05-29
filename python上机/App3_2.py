class ShortInputException(Exception):
    '''自定义异常类'''
    def __init__(self,length):
        Exception.__init__(self)
        self.length=length


try:
    s=input('请输入一个三位数：')
    if (s.__len__() == 0):
        raise EOFError
    if not(len(s)==3 and str.isdigit(s)):
        raise ShortInputException(len(s))
    else:
        print('未发生异常')
except EOFError:
        print('您输入了一个结束标记EOF')
except ShortInputException as x:
        print('ShortInputException:输入的不是三位数')
    
        
        
    
