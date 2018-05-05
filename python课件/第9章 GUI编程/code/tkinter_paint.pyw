import tkinter
from PIL import Image

app = tkinter.Tk()
app.title('My Paint----by Dong Fuguo')
app['width'] = 800
app['height'] = 600

#控制是否允许画图的变量，1：允许，0：不允许
yesno = tkinter.IntVar(value=0)
#控制画图类型的变量，1：曲线，2：直线，3：矩形，4：文本，5：橡皮
what = tkinter.IntVar(value=1)
#记录鼠标位置的变量
X = tkinter.IntVar(value=0)
Y = tkinter.IntVar(value=0)
#前景色
foreColor = '#000000'
backColor = '#FFFFFF'

#创建画布
image = tkinter.PhotoImage()
canvas = tkinter.Canvas(app, bg='white', width=800, height=600)
canvas.create_image(800, 600, image=image)
#鼠标左键单击，允许画图
def onLeftButtonDown(event):
    yesno.set(1)
    X.set(event.x)
    Y.set(event.y)
    if what.get()==4:
        canvas.create_text(event.x, event.y, text=text)
canvas.bind('<Button-1>', onLeftButtonDown)

#记录最后绘制图形的id
lastDraw = 0
#按住鼠标左键移动，画图
def onLeftButtonMove(event):
    if yesno.get()==0:
        return
    if what.get()==1:
        #使用当前选择的前景色绘制曲线
        canvas.create_line(X.get(), Y.get(), event.x, event.y, fill=foreColor)
        X.set(event.x)
        Y.set(event.y)
    elif what.get()==2:
        #绘制直线，先删除刚刚画过的直线，再画一条新的直线
        global lastDraw
        try:
            canvas.delete(lastDraw)
        except Exception as e:
            pass
        lastDraw = canvas.create_line(X.get(), Y.get(), event.x, event.y,
                                      fill=foreColor)
    elif what.get()==3:
        #绘制矩形，先删除刚刚画过的矩形，再画一个新的矩形
        global lastDraw
        try:
            canvas.delete(lastDraw)
        except Exception as e:
            pass
        lastDraw = canvas.create_rectangle(X.get(), Y.get(), event.x, event.y,
                                           fill=backColor, outline=foreColor)
    elif what.get()==5:
        #橡皮，使用背景色填充10*10的矩形区域
        canvas.create_rectangle(event.x-5, event.y-5, event.x+5, event.y+5,
                                outline=backColor, fill=backColor)
canvas.bind('<B1-Motion>', onLeftButtonMove)

#鼠标左键抬起，不允许画图
def onLeftButtonUp(event):
    if what.get()==2:
        #绘制直线
        canvas.create_line(X.get(), Y.get(), event.x, event.y, fill=foreColor)
    elif what.get()==3:
        #绘制矩形
        canvas.create_rectangle(X.get(), Y.get(), event.x, event.y,
                                fill=backColor, outline=foreColor)
    yesno.set(0)
    global lastDraw
    lastDraw = 0
canvas.bind('<ButtonRelease-1>', onLeftButtonUp)

#创建菜单
menu = tkinter.Menu(app, tearoff=0)
#打开图像文件
def Open():
    filename = tkinter.filedialog.askopenfilename(title='Open Image',
                                                  filetypes=[('image', '*.jpg *.png *.gif')])
    if filename:
        global image
        image = tkinter.PhotoImage(file=filename)
        canvas.create_image(80, 80, image=image)
menu.add_command(label='Open', command=Open)
#添加菜单，清除
def Clear():
    for item in canvas.find_all():
        canvas.delete(item)
menu.add_command(label='Clear', command=Clear)
#添加分割线
menu.add_separator()
#创建子菜单，用来选择绘图类型
menuType = tkinter.Menu(menu, tearoff=0)
def drawCurve():
    what.set(1)
    print(what.get())
menuType.add_command(label='Curve', command=drawCurve)
def drawLine():
    what.set(2)
menuType.add_command(label='Line', command=drawLine)
def drawRectangle():
    what.set(3)
menuType.add_command(label='Rectangle', command=drawRectangle)
def drawText():
    global text
    text = tkinter.simpledialog.askstring(title='Input what you want to draw',
                                          prompt='')
    what.set(4)
menuType.add_command(label='Text', command=drawText)
menuType.add_separator()
#选择前景色
def chooseForeColor():
    global foreColor
    foreColor = tkinter.colorchooser.askcolor()[1]
menuType.add_command(label='Choose Foreground Color', command=chooseForeColor)
#选择背景色
def chooseBackColor():
    global backColor
    backColor = tkinter.colorchooser.askcolor()[1]
menuType.add_command(label='Choose Background Color', command=chooseBackColor)
#橡皮
def onErase():
    what.set(5)
menuType.add_command(label='Erase', command=onErase)
menu.add_cascade(label='Type', menu=menuType)

#鼠标右键抬起，弹出菜单
def onRightButtonUp(event):
    menu.post(event.x_root, event.y_root)
canvas.bind('<ButtonRelease-3>', onRightButtonUp)
canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)

app.mainloop()
