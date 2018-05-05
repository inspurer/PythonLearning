import ctypes
msvcrt=ctypes.cdll.LoadLibrary('msvcrt')
printf=msvcrt.wprintf
printf('%s'%'Hello world!')
