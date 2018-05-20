import pickle
tablename = '学生0905160212成绩表'
tabledata= {'inspurer':{'数学':100,'语文':99},'月小水长':{'数学':99,'语文':100}}
#with语句会自动关闭文件流？？？
with open('score.dat','wb') as wfp:
    pickle.dump(tablename,wfp)
    pickle.dump(tabledata,wfp)
#不能合两句with为一，汇报Ran out of input,因为还没写就打开文件了，类似于NP
with open('score.dat','rb') as rfp:
    readname = pickle.load(rfp)
    readdata = pickle.load(rfp)
print('文件头信息(表名为:',readname)
print('表格信息为:',readdata)


