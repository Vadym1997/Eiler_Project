def sum_divisor3or5(bound):
    s = 0
    for i in range(1, bound):
        if i % 5 == 0 or i % 3 == 0:
            s += i
    return s


print(sum_divisor3or5(1000))
