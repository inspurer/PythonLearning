def add(value1, value2):
    #下面一对三引号之间是测试代码，doctest会搜索这些代码并执行
    #并且根据执行结果与预期结果的匹配程度来测试代码是否正确
    '''return the addition of two numbers or the concatenation of two string/list/tuple
    >>> add(3, 5)
    8
    >>> add(3.0, 5.0)
    8.0
    >>> add([1,2], [3, 4])
    [1, 2, 3, 4]
    >>> add((1,), (2, 3, 4))
    (1, 2, 3, 4)
    >>> add(1, [3])
    Traceback (most recent call last):
        ...
    TypeError: value1 and value2 must be of the same type
    >>> add(1, '2')
    Traceback (most recent call last):
        ...
    TypeError: value1 and value2 must be of the same type
    >>> add([1], (2,))
    Traceback (most recent call last):
        ...
    TypeError: value1 and value2 must be of the same type
    >>> add('1234', [1,2,3,4])
    Traceback (most recent call last):
        ...
    TypeError: value1 and value2 must be of the same type
    >>> add({1,2,3}, {3,4,5})
    {1, 2, 3, 4, 5}
    >>> add({1:1}, {2:2})
    Traceback (most recent call last):
        ...
    TypeError: value1 and value2 must be the type of int,float,str,list,tuple or set
    '''
    #下面是正式的功能代码
    if type(value1) not in (int, float, str, list, tuple, set):
        raise TypeError('value1 and value2 must be the type of int,float,str,list,tuple or set')
    if type(value1) != type(value2):
        raise TypeError('value1 and value2 must be of the same type')
    if type(value1) == set:
        return value1 | value2
    else:
        return value1 + value2

if __name__ == "__main__":    
    import doctest
    doctest.testmod()
    print(add(3,5))
