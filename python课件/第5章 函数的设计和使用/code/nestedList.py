def flatList(lst):
    result = []    #存放最终结果
    def nested(lst):#函数嵌套定义
        for item in lst:
            if isinstance(item, list):
                nested(item)#递归子列表
            else:
                result.append(item)#扁平化列表
    nested(lst) #调用嵌套定义的函数
    return result #返回结果

#测试
lst = [1, 2, 3, 4]
print(flatList(lst))

lst = [1, [2, 3], 4]
print(flatList(lst))

lst = [1, [2, [3, 4]]]
print(flatList(lst))

lst = [1, [2, [3, [4]]]]
print(flatList(lst))
