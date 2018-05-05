data = []
with open('sample.txt', 'r') as fp:
    while True:
        line = fp.readline()
        if not line:
            break
        line = line.split()
        line = map(int, line)
        data.extend(line)
        
data.sort()
data = list(map(str, data))

lines = []
for index in range(0, len(data), 4):
    line = '    '.join(data[index:index+4])+'\n'
    lines.append(line)

with open('sample_asc.txt', 'w') as fp:
    fp.writelines(lines)
