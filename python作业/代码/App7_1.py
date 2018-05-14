with open('7_1old.txt','r') as old,open('7_1new.txt','w') as new:
    for line in old:
        new.write(line.swapcase())
    
