# -*- coding: cp936 -*-
import numpy as np
from xlwt import *
book=Workbook()
sheet1=book.add_sheet(u'随机数')
head=['normal','power','gamma','SUM']
N=100
data=np.vstack([np.random.normal(size=N),np.random.power(a=1.0,size=N),np.random.gamma(0.9,size=N)])
al=Alignment()
al.horz=Alignment.HORZ_CENTER
al.vert=Alignment.VERT_CENTER
borders=Borders()
borders.bottom=Borders.THICK
style=XFStyle()
style.alignment=al
style.borders=borders
row0=sheet1.row(0)
for i,text in enumerate(head):
    row0.write(i,text,style=style)
for i,line in enumerate(data):
    for j,value in enumerate(line):
        sheet1.write(j+1,i,value)
for i in xrange(N):
    sheet1.row(i+1).set_cell_formula(3,Formula('sum(A%s:C%s)'%(i+2,i+2)),calc_flags=1)
for i in xrange(4):
    sheet1.col(i).width=4000
sheet1.row(0).height_mismatch=1
sheet1.row(0).height=1000
book.save('tmp.xls')
