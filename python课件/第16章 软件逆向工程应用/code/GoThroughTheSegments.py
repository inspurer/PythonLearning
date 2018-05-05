# -*- coding: cp936 -*-
#第一种版本
segments=dict()
for seg_ea in Segments():
    data=[]
    for ea in range(seg_ea,SegEnd(seg_ea)):
        data.append(chr(Byte(ea)))
    segments[SegName(seg_ea)]=''.join(data)
for seg_name,seg_data in segments.items():
    print seg_name,len(seg_data)
#第二种版本
##segments=dict()
##for seg_ea in Segments():
##    segments[SegName(seg_ea)]=SegEnd(seg_ea)-seg_ea
##for seg_name,seg_data in segments.items():
##    print seg_name,seg_data
