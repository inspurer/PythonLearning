# -*- coding:utf-8 -*-
# Filename: FindPotentialGadgets.py
# --------------------
# Function description:
#   IDAPython program
#   Find potential gadgets of given PE file, use in IDA
# --------------------
# Author: Dong Fuguo
# QQ: 306467355
# Email: dongfuguo2005@126.com
#--------------------
# Date: 2014-11-24
# --------------------
import time
import re
instructions = []
controlInstructions = ('call','ret','retn','jmp','jz','je','jnz','jne',
                       'js','jns','jo','jno','jp','jpe','jnp','jpo','jc',
                       'jb','jnae','jbe','jna','jnc','jnb','jae','jnbe',
                       'ja','jl','jnge','jnl','jge','jle','jng','jnle',
                       'jg','jcxz','jecxz')
def ReadInstructions():
    for seg_ea in Segments():
        for head in Heads(seg_ea,SegEnd(seg_ea)):
            if isCode(GetFlags(head)):
                #here using GetMnem(head) can get only mnemonic
                instruction = GetDisasm(head)
                instructions.append((hex(head),instruction))
                
    '''with open(r'c:\instructions.txt','w') as fp:
        for i in instructions:
            print >>fp, i'''
    #print all the direct or indirect control instructions
    print 'The number of all instructions found is:',len(instructions)
    print 'And the direct or indirect control instructions are:'
    allControlInstructionsCount = 0 #the number of control instructions

    #get all the mnemonics from instructions
    mnemonics = [t[1].split()[0] for t in instructions]

    for ins in controlInstructions:
        if ins in mnemonics:
            print ins,mnemonics.count(ins)
            allControlInstructionsCount = allControlInstructionsCount+mnemonics.count(ins)
    print 'The number of all control instructions is:',allControlInstructionsCount

#check if given instruction is a indirect control diversion instruction
def Check(instruction):
    if instruction.startswith('ret') or instruction.startswith('retn'):
        return True
    else:
        for instr in controlInstructions:
            if instr in ('ret', 'retn'):
                continue
            if instruction.startswith(instr + '    e'):#like call edi
                return True
        return False

#output the potential gadget
def Output(start, end):
    #print >>fp, '='*30
    print '='*30
    for i in range(start, end+1):
        #print >>fp, instructions[i]
        print instructions[i]
    
#find potential gadgets
def FindGadgets():
    total = len(instructions)
    gadgetNumber = 0
    #traverse all instructions reversely
    #for index in range(total-1, -1, -1):
    index = total - 1
    while index >= 0:
        instruction = instructions[index]
        if Check(instruction[1]):
            gadgetNumber += 1
            for i in range(1, 20):
                if Check(instructions[index - i][1]):
                    Output(index - i + 1, index)
                    index = index - i
                    break
            else:
                Output(index -19, index)
                index -= 19
        else:
            index -= 1
    #print >>fp, '='*30
    #print >>fp, 'Total number of gadgets:', gadgetNumber
    print '='*30
    print 'Total number of gadgets:', gadgetNumber

start = time.time()
ReadInstructions()
#fp = open(r'c:\potentialGadgets.txt', 'a')
FindGadgets()
#fp.close()
print time.time() - start
