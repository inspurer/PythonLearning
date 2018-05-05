#use dict method1
data = ['a','2',2,3,6,'2','b',4,7,2,'6','d',6,'a','z']
frequences=dict()
for item in data:
    if item in frequences:
        frequences[item] += 1
    else:
        frequences[item] = 1
print frequences




#use dict method2
frequences = dict()
for item in data:
    frequences[item] = frequences.get(item,0) + 1
print frequences




#use defaultdict
from collections import defaultdict
frequences = defaultdict(int)
for item in data:
    frequences[item] += 1
print frequences.items()




#use set and list type
count_set = set(data)
count_list = []
for item in count_set:
    count_list.append((item,data.count(item)))
print count_list




#use collections.Counter
from collections import Counter
frequences = Counter(data)
print frequences.items()
print list(frequences.elements())    #list all the elements
print frequences.most_common(3)       #list the top 3 elements which have the highest frequence
print frequences['aaa']   #return 0 if the required key does not exist
anotherData = ['a','b','c','d','z',1,2,3]
frequences.update(anotherData)
print frequences.items()    #try:print frequences.items()[0][0]
frequences.subtract(anotherData)
print frequences.items()
