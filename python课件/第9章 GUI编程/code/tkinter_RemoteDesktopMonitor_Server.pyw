import tkinter
import socket
import time
import threading
import struct
from PIL import Image, ImageTk

def updateCanvas(canvas):
    global imageId
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 10600))
    sock.listen(1)
    while running.get() == 1:
        #自适应当前监控窗口大小
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        conn, addr = sock.accept()
        tempImageBytes = b''
        #图像字节数量
        len_head = struct.calcsize('I128sI')
        data = conn.recv(len_head)
        length, size ,sizeLength= struct.unpack('I128sI',data)
        length = int(length)
        rest = length
        bufferSize = 1024*10
        size = eval(size[:int(sizeLength)])
        while running.get() == 1:
            if rest > bufferSize:
                data = conn.recv(1024*10)
            else:
                data = conn.recv(rest)
            tempImageBytes += data
            rest = rest - len(data)
            
            #远程桌面截图接收完成，显示图像
            if rest == 0:
                tempImage = Image.frombytes('RGB', size, tempImageBytes)
                tempImage = tempImage.resize((width,height))
                #tempImage.save('temp.png')
                tempImage = ImageTk.PhotoImage(tempImage)
                #清除上一个截图
                try:
                    canvas.delete(imageId)
                except:
                    pass
                imageId = canvas.create_image(width//2, height//2, image=tempImage)
                #canvas.update()
                #通知客户端可以发送下一个截图
                conn.send(b'ok')
                print('ok')
                break
            
        conn.close()
        
        
        

root = tkinter.Tk()
#主程序窗口位置和大小
root.geometry('640x480+400+300')
width = 640
height = 480
root.title('远程桌面监考系统v1.0---董付国')

#用来表示监控软件是否运行的变量
running = tkinter.IntVar(root, 1)

#关闭监控窗口时触发的消息处理代码
def closeWindow():
    running.set(0)
    root.destroy()
root.protocol('WM_DELETE_WINDOW', closeWindow)

canvas = tkinter.Canvas(root, width=width, height=height)
canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)
#使用子线程刷新监控窗口
t = threading.Thread(target=updateCanvas, args=(canvas,))
#主线程关闭时强制关闭刷新窗口的子线程
t.daemon = True
t.start()
root.mainloop()
