import tkinter

class myWindow:
    def __init__(self, root, myTitle, flag):
        self.top = tkinter.Toplevel(root, width=300, height=200)
        self.top.title(myTitle)
        self.top.attributes('-topmost', 1)
        if flag==1:
            label = tkinter.Label(self.top, text=myTitle)
            label.place(x=50, y=50)
        elif flag==2:
            def buttonOK():
                tkinter.messagebox.showinfo(title='Python V5', message='I am Dong Fuguo')
            button = tkinter.Button(self.top, text=myTitle, command=buttonOK)
            button.place(x=50, y=50)

root = tkinter.Tk()
root.config(width=400)
root.config(height=200)

window1 = tkinter.IntVar(root, value=0)
window2 = tkinter.IntVar(root, value=0)

root.title('Multiple Windows Demo------Dong Fuguo')
def buttonClick1():
    if window1.get()==0:
        window1.set(1)
        w1 = myWindow(root, 'First Window', 1)
        button1.wait_window(w1.top)
        window1.set(0)
button1 = tkinter.Button(root, text='First Window', command=buttonClick1)
button1.place(x=70, y=40, height=40, width=200)

def buttonClick2():
    if window2.get()==0:
        window2.set(1)
        w1 = myWindow(root, 'Second Window', 2)
        button2.wait_window(w1.top)
        window2.set(0)
button2 = tkinter.Button(root, text='Second Window', command=buttonClick2)
button2.place(x=70, y=100, height=40, width=200)
root.mainloop()
