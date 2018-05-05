function_chunks=[]

for ea in Functions():
    func_iter=idaapi.func_tail_iterator_t(idaapi.get_func(ea))

    status=func_iter.main()
    while status:
        chunk=func_iter.chunk()
        function_chunks.append((chunk.startEA,chunk.endEA))
        status=func_iter.next()

for chunk in function_chunks:
    print (hex(chunk[0]),hex(chunk[1])),'belongs to function:',GetFunctionName(chunk[0])
    
