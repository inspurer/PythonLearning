def cni(n, i):
    if n==i or i==0:
        return 1
    return cni(n-1, i) + cni(n-1, i-1)

print(cni(5,4))
