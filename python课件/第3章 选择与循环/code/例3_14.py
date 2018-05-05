import random

x = []
while True:
    if len(x)==20:
        break
    n = random.randint(1, 100)
    if n not in x:
        x.append(n)
print(x)
print(len(x))
print(sorted(x))
