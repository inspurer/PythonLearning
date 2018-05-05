def func(score):
    degree = 'DCBAAE'
    if score > 100 or score < 0:
        return 'wrong score.must between 0 and 100.'
    else:
        index = (score - 60) // 10
        if index >= 0:
            return degree[index]
        else:
            return degree[-1]

print(func(96))
