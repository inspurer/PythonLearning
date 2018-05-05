#Walk the segments
for seg in Segments():
    print SegName(seg),'(',hex(SegStart(seg)),',',hex(SegEnd(seg)),')'
