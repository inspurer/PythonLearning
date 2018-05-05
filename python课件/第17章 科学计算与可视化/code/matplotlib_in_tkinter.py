import sys
import tkinter as Tk
import matplotlib
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

matplotlib.use('TkAgg')

root = Tk.Tk()
root.title("matplotlib in TK")
#设置图形尺寸与质量
f = Figure(figsize=(5, 4), dpi=100)
a = f.add_subplot(111)
t = arange(0.0, 3, 0.01)
s = sin(2*pi*t)
#绘制图形
a.plot(t, s)


#把绘制的图形显示到tkinter窗口上
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
#把matplotlib绘制图形的导航工具栏显示到tkinter窗口上
toolbar = NavigationToolbar2TkAgg(canvas, root)
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

#定义并绑定键盘事件处理函数
def on_key_event(event):
    print('you pressed %s' % event.key)
    key_press_handler(event, canvas, toolbar)
canvas.mpl_connect('key_press_event', on_key_event)

#按钮单击事件处理函数
def _quit():
    #结束事件主循环，并销毁应用程序窗口
    root.quit()
    root.destroy()
button = Tk.Button(master=root, text='Quit', command=_quit)
button.pack(side=Tk.BOTTOM)

Tk.mainloop()
