#print all the functions and their address
for segment in Segments():
    for function_ea in Functions(SegStart(segment),SegEnd(segment)):
        print hex(function_ea),GetFunctionName(function_ea)
