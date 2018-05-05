import sqlite3
import tkinter
import tkinter.ttk
import tkinter.messagebox

def doSql(sql):
    '''用来执行SQL语句，尤其是INSERT和DELETE语句'''    
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()

#创建tkinter应用程序窗口
root = tkinter.Tk()
#设置窗口大小和位置
root.geometry('500x500+400+300')
#不允许改变窗口大小
root.resizable(False, False)
#设置窗口标题
root.title('通信录管理系统')

#在窗口上放置标签组件和用于输入姓名的文本框组件
lbName = tkinter.Label(root, text='姓名：')
lbName.place(x=10, y=10, width=40, height=20)
entryName = tkinter.Entry(root)
entryName.place(x=60, y=10, width=150, height=20)

#在窗口上放置标签组件和用于选择性别的组合框组件
lbSex = tkinter.Label(root, text='性别：')
lbSex.place(x=220, y=10, width=40, height=20)
comboSex = tkinter.ttk.Combobox(root, values=('男', '女'))
comboSex.place(x=270, y=10, width=150, height=20)

#在窗口上放置标签组件和用于输入年龄的文本框组件
lbAge = tkinter.Label(root, text='年龄：')
lbAge.place(x=10, y=50, width=40, height=20)
entryAge = tkinter.Entry(root)
entryAge.place(x=60, y=50, width=150, height=20)

#在窗口上放置标签组件和用于输入部门的文本框组件
lbDepartment = tkinter.Label(root, text='部门：')
lbDepartment.place(x=220, y=50, width=40, height=20)
entryDepartment = tkinter.Entry(root)
entryDepartment.place(x=270, y=50, width=150, height=20)

#在窗口上放置标签组件和用于输入电话号码的文本框组件
lbTelephone = tkinter.Label(root, text='电话：')
lbTelephone.place(x=10, y=90, width=40, height=20)
entryTelephone = tkinter.Entry(root)
entryTelephone.place(x=60, y=90, width=150, height=20)

#在窗口上放置标签组件和用于输入QQ号码的文本框组件
lbQQ = tkinter.Label(root, text='QQ：')
lbQQ.place(x=220, y=90, width=40, height=20)
entryQQ = tkinter.Entry(root)
entryQQ.place(x=270, y=90, width=150, height=20)

#在窗口上放置用来显示通信录信息的表格，使用Treeview组件实现
frame = tkinter.Frame(root)
frame.place(x=0, y=180, width=480, height=280)
#滚动条
scrollBar = tkinter.Scrollbar(frame)
scrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
#Treeview组件
treeAddressList = tkinter.ttk.Treeview(frame, columns=('c1', 'c2', 'c3','c4', 'c5', 'c6'),
                                       show="headings", yscrollcommand = scrollBar.set)
treeAddressList.column('c1', width=70, anchor='center')
treeAddressList.column('c2', width=40, anchor='center')
treeAddressList.column('c3', width=40, anchor='center')
treeAddressList.column('c4', width=120, anchor='center')
treeAddressList.column('c5', width=100, anchor='center')
treeAddressList.column('c6', width=90, anchor='center')
treeAddressList.heading('c1', text='姓名')
treeAddressList.heading('c2', text='性别')
treeAddressList.heading('c3', text='年龄')
treeAddressList.heading('c4', text='部门')
treeAddressList.heading('c5', text='电话')
treeAddressList.heading('c6', text='QQ')
treeAddressList.pack(side=tkinter.LEFT, fill=tkinter.Y)
#Treeview组件与垂直滚动条结合
scrollBar.config(command=treeAddressList.yview)

def bindData():
    '''把数据库里的通信录记录读取出来，然后在表格中显示'''
    #删除表格中原来的所有行
    for row in treeAddressList.get_children():
        treeAddressList.delete(row)
    #读取数据
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM addressList ORDER BY id ASC')
    temp = cur.fetchall()
    conn.close()
    
    #把数据插入表格
    for i, item in enumerate(temp):
        treeAddressList.insert('', i, values=item[1:])

#调用函数，把数据库中的记录显示到表格中
bindData()

#定义Treeview组件的左键单击事件，并绑定到Treeview组件上
#单击鼠标左键，设置变量nameToDelete的值，然后可以使用“删除”按钮来删除
nameToDelete = tkinter.StringVar('')
def treeviewClick(event):
    if not treeAddressList.selection():
        return
    item = treeAddressList.selection()[0]
    nameToDelete.set(treeAddressList.item(item, 'values')[0])
treeAddressList.bind('<Button-1>', treeviewClick)


#在窗口上放置用于添加通信录的按钮，并设置按钮单击事件函数
def buttonAddClick():
    #检查姓名
    name = entryName.get().strip()
    if name == '':
        tkinter.messagebox.showerror(title='很抱歉', message='必须输入姓名')
        return
    #姓名不能重复
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute('SELECT COUNT(id) from addressList where name="' + name + '"')
    c = cur.fetchone()[0]
    conn.close()
    if c!=0:
        tkinter.messagebox.showerror(title='很抱歉', message='姓名不能重复')
        return
    #获取选择的性别
    sex = comboSex.get()
    #检查年龄
    age = entryAge.get().strip()
    if not age.isdigit():
        tkinter.messagebox.showerror(title='很抱歉', message='年龄必须为数字')
        return
    if not 1<int(age)<100:
        tkinter.messagebox.showerror(title='很抱歉', message='年龄必须在1到100之间')
        return
    #检查部门
    department = entryDepartment.get().strip()
    if department == '':
        tkinter.messagebox.showerror(title='很抱歉', message='必须输入部门')
        return
    #检查电话号码
    telephone = entryTelephone.get().strip()
    if telephone=='' or (not telephone.isdigit()):
        tkinter.messagebox.showerror(title='很抱歉', message='电话号码必须是数字')
        return
    #检查QQ号码
    qq = entryQQ.get().strip()
    if qq=='' or (not qq.isdigit()):
        tkinter.messagebox.showerror(title='很抱歉', message='QQ号码必须是数字')
        return
    #所有输入都通过检查，插入数据库
    sql = 'INSERT INTO addressList(name,sex,age,department,telephone,qq) VALUES("'
    sql += name + '","' + sex + '",' + age + ',"' + department + '","'
    sql += telephone + '","' + qq + '")'
    doSql(sql)
    #添加记录后，更新表格中的数据
    bindData()
buttonAdd = tkinter.Button(root, text='添加', command=buttonAddClick)
buttonAdd.place(x=120, y=140, width=80, height=20)

#在窗口上放置用于删除通信录的按钮，并设置按钮单击事件函数
def buttonDeleteClick():
    name = nameToDelete.get()
    if name == '':
        tkinter.messagebox.showerror(title='很抱歉', message='请选择一条记录')
        return
    #如果已经选择了一条通信录，执行SQL语句将其删除
    sql = 'DELETE FROM addressList where name="' + name + '"'
    doSql(sql)
    tkinter.messagebox.showinfo('恭喜', '删除成功')
    #重新设置变量为空字符串
    nameToDelete.set('')
    #更新表格中的数据
    bindData()
buttonDelete = tkinter.Button(root, text='删除', command=buttonDeleteClick)
buttonDelete.place(x=240, y=140, width=80, height=20)

root.mainloop()
