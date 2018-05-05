# -*- coding: cp936 -*-
#给所有助记符着色，还没成功
for seg in Segments():
    for head in Heads(seg,SegEnd(seg)):
        if isCode(GetFlags(head)):
            SetColor(head,CIC_ITEM,0xffffff)
