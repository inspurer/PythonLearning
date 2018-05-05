#Q 编写程序,因式分解从键盘输入的整数
#Sample intput: 48
#Sample output: 48=2*2*2*2*3
import math
x = int(input('Please input an integer:'))
i=2
result = []
t = x;
while i<math.sqrt(x):
    if t==1:
        break
    if t%i==0:
        result.append(i)
        t = t/i
    else: i+=1
print (x,'=','*'.join(map(str,result)))
