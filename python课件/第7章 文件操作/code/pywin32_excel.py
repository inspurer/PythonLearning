import os
import sys
import string
import operator
import win32com.client
class easyExcel:
    def __init__(self, filename=None):
        self.xlApp = win32com.client.Dispatch('Excel.Application')
        if filename:
            self.filename = filename
            self.xlBook = self.xlApp.Workbooks.Open(filename)
        else:
            self.xlBook = self.xlApp.Workbooks.Add()
            self.filename = '' 
   
    def save(self, newfilename=None):
        if newfilename:
            self.filename = newfilename
            self.xlBook.SaveAs(newfilename)
        else:
            self.xlBook.Save() 
    def close(self):
        self.xlBook.Close(SaveChanges=0)
        del self.xlApp
       
    def getCell(self, sheet, row, col):
        "Get value of one cell"
        sht = self.xlBook.Worksheets(sheet)
        return sht.Cells(row, col).Value
    def setCell(self, sheet, row, col, value):
        "set value of one cell"
        sht = self.xlBook.Worksheets(sheet)
        sht.Cells(row, col).Value = value
    def getRange(self, sheet, row1, col1, row2, col2):
        "return a 2d array (i.e. tuple of tuples)"
        sht = self.xlBook.Worksheets(sheet)
        return sht.Range(sht.Cells(row1, col1), sht.Cells(row2, col2)).Value
   
    def setRange(self, sheet, leftCol, topRow, data):
        """insert a 2d array starting at given location.
        Works out the size needed for itself"""       
        bottomRow = topRow + len(data) - 1
        rightCol = leftCol + len(data[0]) - 1
        sht = self.xlBook.Worksheets(sheet)
        #清空所当前sheet里的有单元格
        sht.Cells.Clear()
        sht.Range(
            sht.Cells(topRow, leftCol),
            sht.Cells(bottomRow, rightCol)
            ).Value = data
        sht.Range(
            sht.Cells(topRow, leftCol),
            sht.Cells(topRow, rightCol)
            ).Font.Bold = True
       
    def getContiguousRange(self, sheet, row, col):
        """Tracks down and across from top left cell until it
        encounters blank cells; returns the non-blank range.
        Looks at first row and column; blanks at bottom or right
        are OK and return None witin the array"""
        sht = self.xlBook.Worksheets(sheet)
        # find the bottom row
        bottom = row
        while sht.Cells(bottom + 1, col).Value not in [None, '']:
            bottom = bottom + 1
        # right column
        right = col
        while sht.Cells(row, right + 1).Value not in [None, '']:
            right = right + 1
        #设置第一行若干列为粗体
        return sht.Range(sht.Cells(row, col), sht.Cells(bottom, right)).Value

if __name__ == "__main__":
    filename = ''
    newfilename = ''
    l = len(sys.argv)
    if l==1:
        filename = raw_input("Please enter your '.xls' file name: ")
        newfilename = filename + '.out.xls'
    elif l==2:
        filename = sys.argv[1]
        newfilename = filename + '.out.xls'
    xls = easyExcel(filename)
    val = xls.getContiguousRange('KEGG', 1, 1)
    assert val[0] == ('PathwayName',
                      'Total',
                      'Pvalue',
                      'Qvalue',
                      'Gene',
                      'InputSymbol'), 'Column structure is wrong!'
    rows = [val[1]]
    for row in val[2:]:
        (pn, t, fmt_pv, qv, fmt_gene, fmt_ins) = row
        pv = string.atof(fmt_pv)
        gene = fmt_gene
        ins = fmt_ins
        for i in range(len(rows)):
            r = rows[i]
            if pn==r[0]:
                gene = r[4] + ';' + fmt_gene
                ins = r[5] + ';' + fmt_ins
                rows.remove(rows[i])
                break
        rows.append((pn, t, pv, qv, gene, ins))
    rows = sorted(rows, key=operator.itemgetter(2))
    rows.insert(0, val[0])
    newval = tuple(rows)
    xls.setRange('KEGG', 1, 1, newval)
    xls.save(newfilename)
    xls.close()
