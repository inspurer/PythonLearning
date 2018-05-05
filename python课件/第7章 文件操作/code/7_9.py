import pickle
with open('sample_pickle.dat', 'rb') as f:
    n = pickle.load(f) #读出文件的数据个数
    for i in range(n):
            x = pickle.load(f)
            print(x)
