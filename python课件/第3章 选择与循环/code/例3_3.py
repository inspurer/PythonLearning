import time

date = time.localtime()                          #获取当前日期时间
year, month, day = date[:3]
day_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if year%400==0 or (year%4==0 and year%100!=0):   #判断是否为闰年
    day_month[1] = 29

if month==1:
    print(day)
else:
    print(sum(day_month[:month-1])+day)
