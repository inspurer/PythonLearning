# coding=utf-8
# --------------------
# Function description:Find the longest matches in source codes
# --------------------
# Author: Dong Fuguo
# QQ: 306467355
# Email: dongfuguo2005@126.com
#--------------------
# Date: 2014-11-16, updated on 2016-3-26
# --------------------

from os.path import isfile as isfile
from time import time as time

Result = {}
AllLines = []
FileName = r'FindLongestReuse.py'
#FileName = input('Please input the file to check, including full path:')

#Read the content of given file
#Remove all the whitespace string  of every line,
#preserving only one space character between words or operators
#note:The last line does not contain the '\n' character
def PreOperate():
    global AllLines
    with open(FileName, 'r', encoding='utf-8') as fp:
        for line in fp:
            line = ' '.join(line.split())
            AllLines.append(line)

#Check if the current position is still the duplicated one
def IfHasDuplicated(Index1):
    for item in Result.values():
        for it in item:
            if Index1 == it[0]:
                return it[1] #return the span
    return False

#If the current line Index2 is in a span of duplicated lines, return True, else False
def IsInSpan(Index2):
    for item in Result.values():
        for i in item:
            if i[0] <= Index2 < i[0] + i[1]:
                return True
    return False

def MainCheck():
    global Result
    TotalLen = len(AllLines)
    Index1 = 0
    while Index1 < TotalLen - 1:
        #speed up
        span = IfHasDuplicated(Index1)
        if span:
            Index1 += span
            continue
        Index2 = Index1 + 1
        while Index2 < TotalLen:
            #speed up, skip the duplicated lines
            if IsInSpan(Index2):
                Index2 +=1
                continue
            src = ''
            des = ''
            for i in range(10):                
                if Index2+i >= TotalLen:
                    break                
                src += AllLines[Index1+i]
                des += AllLines[Index2+i]
                if src == des:
                    t = Result.get(Index1, [])
                    for tt in t:
                        if tt[0] == Index2:
                            tt[1] = i+1
                            break
                    else:
                        t.append([Index2, i+1])
                    Result[Index1] = t
                else:
                    break
            t = Result.get(Index1, [])
            for tt in t:
                if tt[0] == Index2:
                    Index2 += tt[1]
                    break
            else:
                Index2 +=1
                
        #Optimize the Result dictionary, remove the items with span<3
        Result[Index1] = Result.get(Index1, [])
        for n in Result[Index1][::-1]: #Note: here must use the reverse slice,
            if n[1] < 3:               
                Result[Index1].remove(n)
        if not Result[Index1]:
            del Result[Index1]

        #Compute the min span of duplicated codes of line Index1,modify the step Index1
        a = [ttt[1] for ttt in Result.get(Index1, [[Index1, 1]])]
        if a:
            Index1 += max(a)
        else:
            Index1 += 1

#Output the result
def Output():    
    print('-'*20)    
    print('Result:')
    for key, value in Result.items():
        print('The original line is: \n {0}'.format(AllLines[key]))
        print('Its line number is {0}'.format(key+1))
        print('The duplicated line numbers are:')
        for i in value:
            print('    Start:', i[0], '    Span:', i[1])
        print('-'*20)
    print('-'*20)

if isfile(FileName):
    start = time()
    PreOperate()
    MainCheck()
    Output()
    print('Time used:', time() - start)
