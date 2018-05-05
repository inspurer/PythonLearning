class Set(object):
    def __init__(self, data=None):
        if data == None:
            self.__data = []
        else:
            if not hasattr(data, '__iter__'):
                #提供的数据不可迭代，实例化失败
                raise Exception('必须提供可迭代的数据类型')
            temp = []
            for item in data:
                #集合中的元素必须可哈希
                hash(item)
                if not item in temp:
                    temp.append(item)
            self.__data = temp

    #析构方法
    def __del__(self):
        del self.__data

    #添加元素，要求元素必须可哈希
    def add(self, value):
        hash(value)
        if value not in self.__data:
            self.__data.append(value)
        else:
            print('元素已存在，操作被忽略')

    #删除元素
    def remove(self, value):
        if value in self.__data:
            self.__data.remove(value)
            print('删除成功')
        else:
            print('元素不存在，删除操作被忽略')

    #随机弹出并返回一个元素
    def pop(self):
        if not self.__data:
            print('集合已空,弹出操作被忽略')
            return
        import random
        item = random.choice(self.__data)
        self.__data.remove(item)
        return item

    #运算符重载，集合差集运算
    def __sub__(self, anotherSet):
        if not isinstance(anotherSet, Set):
            raise Exception('类型错误')
        #空集合
        result = Set()
        #如果一个元素属于当前集合而不属于另一个集合，添加
        for item in self.__data:
            if item not in anotherSet.__data:
                result.__data.append(item)
        return result
    
    #提供方法，集合差集运算，复用上面的代码
    def difference(self, anotherSet):
        return self - anotherSet

    
    #|运算符重载，集合并集运算
    def __or__(self, anotherSet):
        if not isinstance(anotherSet, Set):
            raise Exception('类型错误')
        result = Set(self.__data)
        for item in anotherSet.__data:
            if item not in result.__data:
                result.__data.append(item)
        return result
    
    #提供方法，集合并集运算
    def union(self, anotherSet):
        return self | anotherSet
    
    #&运算符重载，集合交集运算
    def __and__(self, anotherSet):
        if not isinstance(anotherSet, Set):
            raise Exception('类型错误')
        result = Set()
        for item in self.__data:
            if item in anotherSet.__data:
                result.__data.append(item)
        return result
        
    #^运算符重载，集合对称差集
    def __xor__(self, anotherSet):
        return (self-anotherSet) | (anotherSet-self)

    #提供方法，集合对称差集运算
    def symetric_difference(self, anotherSet):
        return self ^ anotherSet

    #==运算符重载，判断两个集合是否相等
    def __eq__(self, anotherSet):
        if not isinstance(anotherSet, Set):
            raise Exception('类型错误')
        if sorted(self.__data) == sorted(anotherSet.__data):
            return True
        return False

    #>运算符重载，集合包含关系
    def __gt__(self, anotherSet):
        if not isinstance(anotherSet, Set):
            raise Exception('类型错误')
        if self != anotherSet:
            flag1 = True
            for item in self.__data:
                if item not in anotherSet.__data:
                    #当前集合中有的元素不属于另一个集合
                    flag1 = False
                    break
            flag2 = True
            for item in anotherSet.__data:
                if item not in self.__data:
                    #另一个集合中有的元素不属于当前集合
                    flag2 = False
                    break
            if  not flag1 and flag2:
                return True
            return False

    #>=运算符重载，集合包含关系
    def __ge__(self, anotherSet):
        if not isinstance(anotherSet, Set):
            raise Exception('类型错误')
        return self==anotherSet or self>anotherSet
    
    #提供方法，判断当前集合是否为另一个集合的真子集
    def issubset(self, anotherSet):
        return self < anotherSet

    #提供方法，判断当前集合是否为另一个集合的超集
    def issuperset(self, anotherSet):
        return self > anotherSet

    #提供方法，清空集合所有元素
    def clear(self):
        while self.__data:
            del self.__data[-1]
        print('集合已清空')

    #运算符重载，使得集合可迭代
    def __iter__(self):
        return iter(self.__data)

    #运算符重载，支持in运算符
    def __contains__(self, value):
        return value in self.__data

    #支持内置函数len()
    def __len__(self):
        return len(self.__data)
        
    #直接查看该类对象时调用该函数
    def __repr__(self):
        return '{'+str(self.__data)[1:-1]+'}'

    #使用print()函数输出该类对象时调用该函数
    __str__ = __repr__
