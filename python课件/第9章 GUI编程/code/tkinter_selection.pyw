import tkinter
import tkinter.messagebox
import tkinter.ttk

#创建tkinter应用程序
root = tkinter.Tk()
#设置窗口标题
root.title('Selection widgets')
#定义窗口大小
root['height'] = 400
root['width'] = 320
#与姓名关联的变量
varName = tkinter.StringVar()
varName.set('')
#创建标签，然后放到窗口上
labelName = tkinter.Label(root, text='Name:',justify=tkinter.RIGHT,width=50)
labelName.place(x=10, y=5, width=50, height=20)
#创建文本框，同时设置关联的变量
entryName = tkinter.Entry(root, width=120,textvariable=varName)
entryName.place(x=70, y=5, width=120, height=20)

labelGrade = tkinter.Label(root, text='Grade:', justify=tkinter.RIGHT, width=50)
labelGrade.place(x=10, y=40, width=50, height=20)
#模拟学生所在年级，字典键为年级，字典值为班级
studentClasses = {'1':['1', '2', '3', '4'],
               '2':['1', '2'],
               '3':['1', '2', '3']}
 #学生年级组合框
comboGrade = tkinter.ttk.Combobox(root,width=50,
                              values=tuple(studentClasses.keys()))
comboGrade.place(x=70, y=40, width=50, height=20)
#事件处理函数
def comboChange(event):
    grade = comboGrade.get()
    if grade:
        #动态改变组合框可选项
        comboClass["values"] = studentClasses.get(grade)
    else:
        comboClass.set([])
#绑定组合框事件处理函数
comboGrade.bind('<<ComboboxSelected>>', comboChange)

labelClass = tkinter.Label(root, text='Class:', justify=tkinter.RIGHT, width=50)
labelClass.place(x=130, y=40, width=50, height=20)
#学生年级组合框
comboClass = tkinter.ttk.Combobox(root, width=50)
comboClass.place(x=190, y=40, width=50, height=20)

labelSex = tkinter.Label(root, text='Sex:', justify=tkinter.RIGHT, width=50)
labelSex.place(x=10, y=70, width=50, height=20)
#与性别关联的变量，1:男；0:女，默认为男
sex = tkinter.IntVar()
sex.set(1)
#单选钮，男
radioMan = tkinter.Radiobutton(root,variable=sex,value=1,text='Man')
radioMan.place(x=70, y=70, width=50, height=20)
#单选钮，女
radioWoman = tkinter.Radiobutton(root,variable=sex,value=0,text='Woman')
radioWoman.place(x=130, y=70, width=70, height=20)
#与是否班长关联的变量，默认当前学生不是班长
monitor = tkinter.IntVar()
monitor.set(0)
#复选框，选中时变量值为1，#未选中时变量值为0
checkMonitor = tkinter.Checkbutton(root,text='Is Monitor?', variable=monitor,
                              onvalue=1, offvalue=0)
checkMonitor.place(x=20, y=100, width=100, height=20)
#添加按钮单击事件处理函数
def addInformation():
    result = 'Name:' + entryName.get()
    result = result + ';Grade:' + comboGrade.get()
    result = result + ';Class:' + comboClass.get()
    result = result + ';Sex:' + ('Man' if sex.get() else 'Woman')
    result = result + ';Monitor:' + ('Yes' if monitor.get() else 'No')
    listboxStudents.insert(0, result)    
buttonAdd = tkinter.Button(root, text='Add',width=40, command=addInformation)
buttonAdd.place(x=130, y=100, width=40, height=20)
#删除按钮的事件处理函数
def deleteSelection():
    selection = listboxStudents.curselection()
    if  not selection:
        tkinter.messagebox.showinfo(title='Information', message='No Selection')
    else:
        listboxStudents.delete(selection)
buttonDelete = tkinter.Button(root, text='DeleteSelection',
                        width=100, command=deleteSelection)
buttonDelete.place(x=180, y=100, width=100, height=20)
#创建列表框组件
listboxStudents = tkinter.Listbox(root, width=300)
listboxStudents.place(x=10, y=130, width=300, height=200)
#启动消息循环
root.mainloop()
