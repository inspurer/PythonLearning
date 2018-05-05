def main(n):
    for i in range(n):
        print((' * '*i).center(n*3))
    for i in range(n, 0, -1):
        print((' * '*i).center(n*3))

main(10)
