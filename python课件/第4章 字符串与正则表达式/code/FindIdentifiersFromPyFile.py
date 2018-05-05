# -*- coding:utf-8 -*-
# Filename: FindIdentifiersFromPyFile.py
# --------------------
# Function description:
#    Find all the identifiers of class, function, and all kinds of variables,
#    using Regular Expression
# --------------------
# Author: Dong Fuguo
# QQ: 306467355
# Email: dongfuguo2005@126.com
#--------------------
# Date: 2014-11-24, Updated on 2016-7-16
# --------------------

import re
import os
import sys

classes = {}
functions = []
variables = {'normal':{}, 'parameter':{}, 'infor':{}}

'''This is a test string:
atest, btest = 3, 5
to verify that variables in comments will be ignored by this algorithm
'''

def _identifyClassNames(index, line):
    '''parameter index is the line number of line,
     parameter line is a line of code of the file to check'''
    pattern = re.compile(r'(?<=class\s)\w+(?=.*?:)')
    matchResult = pattern.search(line)
    if not matchResult:
        return
    className = matchResult.group(0)
    classes[className] = classes.get(className, [])
    classes[className].append(index)

def _identifyFunctionNames(index, line):
    pattern = re.compile(r'(?<=def\s)(\w+)\((.*?)\)(?=:)')
    matchResult = pattern.search(line)
    if not matchResult:
        return
    functionName = matchResult.group(1)
    functions.append((functionName, index))
    parameters = matchResult.group(2).split(r', ')
    if parameters[0] == '':
        return
    for v in parameters:
        variables['parameter'][v] = variables['parameter'].get(v, [])
        variables['parameter'][v].append(index)
    
def _identifyVariableNames(index, line):
    #find normal variables, including the case: a, b = 3, 5
    pattern = re.compile(r'\b(.*?)(?=\s=)')
    matchResult = pattern.search(line)
    if matchResult:
        vs = matchResult.group(1).split(r', ')
        for v in vs:
            #consider the case 'if variable == value'
            if 'if ' in v:
                v = v.split()[1]
            #consider the case: 'a[3] = 3'
            if '[' in v:
                v = v[0:v.index('[')]
            variables['normal'][v] = variables['normal'].get(v, [])
            variables['normal'][v].append(index)
    #find the variables in for statements
    pattern = re.compile(r'(?<=for\s)(.*?)(?=\sin)')
    matchResult = pattern.search(line)
    if matchResult:
        vs = matchResult.group(1).split(r', ')
        for v in vs:
            variables['infor'][v] = variables['infor'].get(v, [])
            variables['infor'][v].append(index)

def output():
    print('='*30)
    print('The class names and their line numbers are:')
    for key, value in classes.items():
        print(key, ':', value)
    print('='*30)
    print('The function names and their line numbers are:')
    for i in functions:
        print(i[0], ':', i[1])
    print('='*30)
    print('The normal variable names and their line numbers are:')
    for key, value in variables['normal'].items():
        print(key, ':', value)
    print('-'*20)
    print('The parameter names and their line numbers in functions are:')
    for key, value in variables['parameter'].items():
        print(key, ':', value)
    print('-'*20)
    print('The variable names and their line numbers in for statements are:')
    for key, value in variables['infor'].items():
        print(key, ':', value)

#suppose the lines of comments less than 50
def comments(index):
    for i in range(50):
        line = allLines[index + i].strip()
        if line.endswith('"""') or line.endswith("'''"):
            return i+1
        
if __name__ == '__main__':
    fileName = sys.argv[1]         #命令行参数
    if not os.path.isfile(fileName):
        print('Your input is not a file.')
        sys.exit(0)                #退出当前程序
    if not fileName.endswith('.py'):
        print('Sorry. I can only check Python source file.')
        sys.exit(0)
    allLines = []
    with open(fileName, 'r') as fp:
        allLines = fp.readlines()        
    index = 0    
    totalLen = len(allLines)
    while index < totalLen:
        line = allLines[index]
        #strip the blank characters at both end of line
        line = line.strip()
        #ignore the comments starting with '#'
        if line.startswith('#'):
            index += 1
            continue
        #ignore the comments between ''' or """
        if line.startswith('"""') or line.startswith("'''"):
            index += comments(index)
            continue
        #identify identifiers
        _identifyClassNames(index+1, line)
        _identifyFunctionNames(index+1, line)
        _identifyVariableNames(index+1, line)
        index += 1
    output()