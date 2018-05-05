times = dict()
for seg_startEA in Segments():
    if SegName(seg_startEA)!='.text':
        continue
    for instEA in Heads(seg_startEA, SegEnd(seg_startEA)):
        if isCode(GetFlags(instEA)):
            mnem = GetMnem(instEA)
            times[mnem] = times.get(mnem, 0)+1

times = sorted(times.items(), key=lambda x: x[1], reverse=True)
for k, v in times:
    print k, ':', v
