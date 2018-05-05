function_chunks=[]
func_iter=idaapi.func_tail_iterator_t(idaapi.get_func(ScreenEA()))
status=func_iter.main()
while status:
    chunk=func_iter.chunk()
    function_chunks.append((hex(chunk.startEA),hex(chunk.endEA)))
    status=func_iter.next()

for t in function_chunks:
    print t
