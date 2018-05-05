# -*- coding: cp936 -*-
persons=[{'name':'Dong','age':37},{'name':'Zhang','age':40},{'name':'Li','age':50},{'name':'Dong','age':43}]
print persons
#使用key来指定排序依据，这里的意思是先按姓名升序排序，姓名相同的按年龄降序排序
print sorted(persons,key=lambda x:(x['name'],-x['age']))



#sorted可用于任意可迭代对象，而sort一般常用于列表
a=(3,5,3,2,1,6,8)
#a.sort()#错误，元组对象没有sort方法
print sorted(a)



#sorted返回排序后的列表，原列表不变；sort函数直接修改原列表，函数返回值为None
a=[1,3,6,2,3,9,10,7]
print sorted(a)
print a
print a.sort()
print a




#对于sort和sorted而言，其key参数只处理一次，而cmp参数会调用多次，因此建议优先使用key参数
from timeit import Timer
print Timer(stmt='sorted(xs,key=lambda x:x[1])',setup='xs=range(100);xs=zip(xs,xs);').timeit(10000)
print Timer(stmt='sorted(xs,cmp=lambda a,b:cmp(a[1],b[1]))',setup='xs=range(100);xs=zip(xs,xs);').timeit(10000)



#使用sorted对字典进行排序
phonebook = {'Linda':'7750','Bob':'9345','Carol':'5834'}
from operator import itemgetter
sorted_pb=sorted(phonebook.iteritems(),key=itemgetter(1))#尝试把1改成0看看结果
print sorted_pb



#使用sorted对多维列表排序
gameresult = [['Bob',95.0,'A'],['Alan',86.0,'C'],['Mandy',83.5,'A'],['Rob',89.3,'E']]
print sorted(gameresult,key=itemgetter(0,1))#尝试改变括号里的数字看看结果



#使用sorted对含有列表的字典排序
mydict={'Li':['M',7],
        'Zhang':['E',2],
        'Wang':['P',3],
        'Du':['C',2],
        'Ma':['C',9],
        'Zhe':['H',7]}
print sorted(mydict.iteritems(),key=lambda (k,v):itemgetter(1)(v))#把(1)(v)改成(0)(v)和(0)(k)看看结果



#使用sorted对含有字典的列表排序
gameresult = [{'name':'Bob','wins':10,'losses':3,'rating':75.0},
              {'name':'David','wins':3,'losses':5,'rating':57.0},
              {'name':'Carol','wins':4,'losses':5,'rating':57.0},
              {'name':'Patty','wins':9,'losses':3,'rating':72.8}]
print sorted(gameresult,key=itemgetter('wins','name'))
