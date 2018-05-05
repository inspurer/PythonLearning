import sqlite3
import speech
import time
conn=sqlite3.connect("StudInfo.db")   #也可使数据库位于当前目录
cur=conn.cursor()
#用日期和星期构成新字段名
newkey=time.strftime("%A%d",time.localtime(time.time()))
#在RollCall表中添加该新字段
#print newkey
#print type(newkey)
#注意：由于字段的唯一性，每个日期只能执行程序一次，如果需要多次实验，请修改一下机器的日期
cur.execute("alter table RollCall add "+newkey+" varchar(6) NULL")
cur.execute("select * from RollCall")
li=cur.fetchall()
#初始化回答列表
response=["ye","here","yes"]
for line in li:
    print(line[1])
    answer="NULL"
    i=1
#每人语音点名在3次以内
    while i<=3: 
        speech.say(line[1])
        answer=speech.input()
        if answer.lower()in response:
            answer_flag="T"
            break
#学生回答，则在回答列表中修改新字段的标记为T,并中断该生语音点名
        else: 
            answer_flag="F"   #书中代码需要如此修改
        i+=1
    cur.execute("update  RollCall  set "+newkey+"='"+answer_flag+"' where stud_id="+str(line[0])+ " ")  #书中代码需要如此修改
    print("%s:%s"%(str(line[1]),answer_flag))
            
conn.commit()
conn.close()
