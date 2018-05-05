def demo(s):
    result = [0, 0]
    for ch in s:
        if 'a'<=ch<='z':
            result[1] += 1
        elif 'A'<=ch<='Z':
            result[0] += 1
return result

print(demo('aaaabbbbC'))
