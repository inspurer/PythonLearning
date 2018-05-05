# -*- coding: cp936 -*-

#列表解析支持多重嵌套
nested_list = [['Hello','World'],['Goodbye','World']]
print [[s.upper() for s in xs] for xs in nested_list]


#列表解析支持多重迭代
print [(a,b) for a in ['a',1,'c'] for b in [1,2,'c',4,'a'] if a !=b]


#列表解析支持复杂表达式
def f(v):
    if v%2 == 0:
        v=v**2
    else:
        v=v+1
    return v
print [f(v) for v in [2,3,4,-1] if v>0]
print [v**2 if v%2 == 0 else v+1 for v in [2,3,4,-1] if v>0]


#列表解析支持任意可迭代对象
fp = open('c:\install.log','r')
print [i for i in fp if 'c:' in i]
fp.close()
