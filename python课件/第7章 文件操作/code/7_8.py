import pickle
i = 13000000
a = 99.056
s = '中国人民123abc'
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
tu = (-5, 10, 8)
coll = {4, 5, 6}
dic = {'a':'apple', 'b':'banana', 'g':'grape', 'o':'orange'}
data = [i, a, s, lst, tu, coll, dic]
with open('sample_pickle.dat', 'wb') as f:
    try:
         pickle.dump(len(data), f)  #表示后面将要写入的数据个数
         for item in data:
              pickle.dump(item, f)
    except:
        print('写文件异常!')  #如果写文件异常则跳到此处执行
