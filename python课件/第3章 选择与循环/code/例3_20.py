#假设能买x只公鸡，x最大为20
for x in range(21):
    #假设能买y只母鸡，y最大为33
    for y in range(34):
        #假设能买z只小鸡
        z = 100-x-y
        if (z%3==0 and 5*x + 3*y + z//3 == 100):
              print(x,y,z)
