from math import gcd

start = 34567
end = 1234567
factor_list = []

for i in range(start, end):
    if i%2==0 or i%3==0 or i%5==0 or i%7==0 or i%11==0:
        factor_list.append(i)

print(sum(factor_list))

# 2, 3, 5, 7, 11], 34567, 1234567)