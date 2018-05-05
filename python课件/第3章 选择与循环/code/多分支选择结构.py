def func(score):
    if score > 100:
        return 'wrong score.must <= 100.'
    elif score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    elif score >= 0:
        return 'E'
    else:
        return 'wrong score.must >0'	

print(func(96))
