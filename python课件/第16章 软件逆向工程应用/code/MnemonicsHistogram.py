mnemonics = dict()
ea = ScreenEA()
for head in Heads(SegStart(ea), SegEnd(ea)):
    if isCode(GetFlags(head)):
        mnem = GetMnem(head)
        mnemonics[mnem] = mnemonics.get(mnem, 0)+1
mnem_list = map(lambda x:(x[1],x[0]), mnemonics.items())
mnem_list.sort()

for cnt,mnem in mnem_list:
    print mnem, cnt
