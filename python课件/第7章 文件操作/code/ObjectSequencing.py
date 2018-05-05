# -*- coding: cp936 -*-
#序列化，简单地说就是把内存中的数据结构在不丢失其身份和类型信息的情况下转成对象的文本或二进制表示的过程，
#对象序列化后的形式经过反序列化过程应该能够恢复为原对象。
#Python中常用的序列化模块有pickle、json、marshal和shelve
#其中pickle有C语言实现的cPickle，速度约提高1000倍。cPickle不能被集成，但不影响大多数应用


#推荐优先使用cPickle，在Linux下序列化的格式文件可以在Windows平台上进行反序列化
import cPickle as pickle
data = {'name':'Dong Fuguo','Age':37,'affiliate':'SDIBT'}
print data
fp=open('pickletest.dat','wb')
pickle.dump(data,fp)
fp.close()

with open('pickletest.dat','rb') as f:
    print pickle.load(f)


#pickle能够自动维护对象间的引用，如果一个对象上存在多个引用，pickle后不会改变对象间的引用，
#并且能够自动处理循环和递归引用
a=['a','b']
b=a
b.append('c')
p=pickle.dumps((a,b))
a1,b1=pickle.loads(p)
print a1
print b1
a1.append('d')
print b1
