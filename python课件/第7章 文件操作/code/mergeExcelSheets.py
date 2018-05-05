import os
import sys
from tkinter import Tk, Button
from tkinter import filedialog
from tkinter import simpledialog

try:
    import openpyxl
except:
    #先把pip升级到最新版本
    path = '"'+os.path.dirname(sys.executable)+'\\scripts\\pip" install --upgrade pip'
    os.system(path)
    #安装openpyxl扩展库
    path = '"'+os.path.dirname(sys.executable)+'\\scripts\\pip" install openpyxl'
    os.system(path)
    import openpyxl

def merge(start):
    #显示打开文件对话框，打开要合并的Excel 2007+文件
    opts= {'filetypes':[('Excel 2007', '.xlsx')]}
    filename = filedialog.askopenfilename(**opts)
    if not filename:
        return
    #分割路径和文件名
    filepath, tempfilename = os.path.split(filename)
    shotname = os.path.splitext(tempfilename)[0]
    #生成的新文件名
    newFile = filepath + '\\' + shotname + '_merge.xlsx'
    #创建新的Excel 2007+文件
    workbook = openpyxl.Workbook()
    #添加新的worksheet
    worksheet = workbook.worksheets[0]
    data = openpyxl.load_workbook(filename)
    for sheetnum, sheet in enumerate(data.worksheets):
        #根据设定的表头行数，设置读取的起始行
        #第一个sheet读取表头，后面的sheet忽略表头
        if sheetnum == 0:
            rowStart = 0
        else:
            rowStart = start
        #遍历原sheet，根据情况忽略表头
        for row in sheet.rows[rowStart:]:
            line = [col.value for col in row]
            worksheet.append(line)
    #保存新文件
    workbook.save(newFile)
    #打开刚刚创建的新文件
    os.startfile(newFile)
    
#单击按钮后执行的函数，参数a表示Excel文件中每个worksheet预期表头行数
def callback():
    kw = {'initialvalue':1, 'minvalue':0, 'maxvalue':10}
    headerNum = simpledialog.askinteger('表头行数', '请输入表头行数',**kw)
    if headerNum != None:
        merge(headerNum)
    
root = Tk()
root.title("合并sheet")
Button(root, text="合并WorkSheets", bg='blue', bd=2,width=28,command=callback).pack()


root.mainloop()
