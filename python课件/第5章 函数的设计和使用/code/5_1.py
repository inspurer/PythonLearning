from math import pi as PI
import types
def CircleArea(r):
    if isinstance(r, (int, float)): #确保接收的参数为数值
        return PI*r*r
    else:
        print('You must give me an integer or float as radius.')

print(CircleArea(3))
