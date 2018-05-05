# -*- coding:utf-8 -*-
# Filename: CheckCodeFormats.py
# --------------------
# Function description:
# Check the code format of given Python source file
# --------------------
# Author: Dong Fuguo
# QQ: 306467355
# Email: dongfuguo2005@126.com
#--------------------
# Date: 2014-12-14, Updated on 2016-7-16
# --------------------

import sys
import re

def checkFormats(lines, desFileName):
    fp = open(desFileName, 'w')
    for i, line in enumerate(lines):
        print('='*30)
        print('Line:', i+1)        
        if line.strip().startswith('#'):
            print(' '*10+'Comments.Pass.')
            fp.write(line)
            continue
        flag = True        
        #check operator symbols
        symbols = [',', '+', '-', '*', '/', '//', '**', '>>', '<<', '+=', '-=', '*=', '/=']
        temp_line = line
        for symbol in symbols:
            pattern = re.compile(r'\s*'+re.escape(symbol)+r'\s*')
            temp_line = pattern.split(temp_line)
            sep = ' '+symbol+' '
            temp_line = sep.join(temp_line)
        if line != temp_line:
            flag = False
            print(' '*10+'You may miss some blank spaces in this line.')        
        #check import statement
        if line.strip().startswith('import'):
            if ',' in line:
                flag = False
                print(' '*10+"You'd better import one module at a time.")
                temp_line = line.strip()
                modules = temp_line[temp_line.index(' ')+1:]
                modules = modules.strip()
                pattern = re.compile(r'\s*,\s*')
                modules = pattern.split(modules)
                temp_line = ''
                for module in modules:
                    temp_line += line[:line.index('import')]+'import '+module+'\n'
                line = temp_line
            pri_line = lines[i-1].strip()
            if pri_line and (not pri_line.startswith('import')) and \
               (not pri_line.startswith('#')):
                flag = False
                print(' '*10+'You should add a blank line before this line.')
                line = '\n'+line
            after_line = lines[i+1].strip()
            if after_line and (not after_line.startswith('import')):
                flag = False
                print(' '*10+'You should add a blank line after this line.')
                line =line+'\n'
        #check if there is a blank line before new funtional code block
        #including the class/function definition
        if line.strip() and not line.startswith(' ') and i > 0:
            pri_line = lines[i-1]
            if pri_line.strip() and pri_line.startswith(' '):
                flag = False
                print(' '*10+"You'd better add a blank line before this line.")
                line = '\n'+line                
        if flag:
            print(' '*10 + 'Pass.')
        fp.write(line)
    fp.close()
            
if __name__ == '__main__':
    fileName = sys.argv[1]            #√¸¡Ó––≤Œ ˝
    fileLines = []
    with open(fileName, 'r') as fp:
        fileLines = fp.readlines()
    desFileName = fileName[:-3]+'_new.py'
    checkFormats(fileLines, desFileName)
    #check the ratio of comment lines to all lines
    comments = [line for line in fileLines if line.strip().startswith('#')]
    ratio = len(comments)/len(fileLines)
    if ratio <= 0.3:
        print('='*30)
        print('Comments in the file is less than 30%.')
        print('Perhaps you should add some comments at appropriate position.')