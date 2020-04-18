factor = 2
num = 600851475143
for factor in range(2, num):
    if num <= factor:
        break
    if num % factor == 0:
        num = num / factor
print(factor)
