def licai(base, rate, days):
    #初始投资金额
    result = base
    #整除，用来计算一年可以滚动多少期
    times = 365//days
    for i in range(times):
        result = result +result*rate/365*days
    return result
#14天理财，利率0.0385，投资10万
print(licai(100000, 0.0385, 14))
