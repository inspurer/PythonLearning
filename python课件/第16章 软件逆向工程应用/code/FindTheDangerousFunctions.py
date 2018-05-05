from idaapi import *

danger_functions=['strcpy','sprintf','strncpy','memcpy']

for func in danger_functions:
    addr=LocByName(func)
    if addr!=BADADDR:
        cross_refs=CodeRefsTo(addr,0)
        print 'Cross References to %s'%func
        print '---------------------------'
        for ref in cross_refs:
            print '%08x'%ref
            SetColor(ref,CIC_ITEM,0x0000ff)
        print '---------------------------'
