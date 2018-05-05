score = [70, 90, 78, 85, 97, 94, 65, 80]
s = 0
for i in score:
	s += i
print(s/len(score))
print(sum(score) / len(score))                 #也可以直接这样做
