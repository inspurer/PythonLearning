# -*- coding: cp936 -*-
#第一个版本
##from sets import Set
##ea=ScreenEA()
##callers=dict()
##callees=dict()
##for function_ea in Functions(SegStart(ea),SegEnd(ea)):#遍历当前段中的函数
##    f_name=GetFunctionName(function_ea)#获取函数名字
##    callers[f_name]=Set(map(GetFunctionName,CodeRefsTo(function_ea,0)))#调用该函数的所有函数
##    for ref_ea in CodeRefsTo(function_ea,0):#遍历调用该函数的所有函数
##        caller_name=GetFunctionName(ref_ea);
##        callees[caller_name]=callees.get(caller_name,Set())
##        callees[caller_name].add(f_name)#
##functions=Set(callees.keys()+callers.keys())
##for f in functions:
##    print '%-4d::%s::%4d'%(len(callers.get(f,[])),f,len(callees.get(f,[])))

#第二个版本，暂时还不能用
from sets import Set
ea=ScreenEA()
callers=dict()
callees=dict()

for function_ea in Functions(SegStart(ea),SegEnd(ea)):
    f_name=GetFunctionName(function_ea)
    callers[f_name]=Set(map(GetFunctionName,CodeRefsTo(function_ea,0)))
    callees[f_name]=Set(map(GetFunctionName,CodeRefsFrom(function_ea,0)))
    
functions=Set(callees.keys()+callers.keys())
for f in functions:
    print '%d:::%s:::%d'%(len(callers.get(f,[])),f,len(callees.get(f,[])))

