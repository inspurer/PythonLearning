import pefile  
import pydasm  
import sys

pe = pefile.PE(r"c:\windows\notepad.exe")  

console = sys.stdout 
f = open('pe_dasm.txt', 'w')
sys.stdout = f

ep = pe.OPTIONAL_HEADER.AddressOfEntryPoint 
ep_ava = ep + pe.OPTIONAL_HEADER.ImageBase 
data = pe.get_memory_mapped_image()[ep:] 
offset = 0 
while offset < len(data): 
    i = pydasm.get_instruction(data[offset:], pydasm.MODE_32)
    instruction = pydasm.get_instruction_string(i, pydasm.FORMAT_INTEL, ep_ava+offset)
    if instruction != None:
        print hex(ep + offset), '\t', instruction
    else:
        break
    try:
        offset += i.length
    except BaseException,e:
        break

f.close()
sys.stdout = console
