def demo(t):
    a, b = 1, 1
    while b<t:
        a, b = b, a+b
    else:
        return b

print(demo(50))
