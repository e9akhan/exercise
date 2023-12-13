from math import gcd, ceil

def solver(factors, start, end):
    total = 0
    total1 = 0

    for i in range(len(factors)):
        total += (factors[i]*((end-1)//factors[i])*((end-1)//factors[i]+1)/2)
        if i>0:
            common = common*factors[i]//gcd(factors[i], common)
        else:
            common = factors[i]

    if len(factors) > 1:
        total -= (common*((end-1)//common)*((end-1)//common+1)/2)
    print(total)

    for i in range(len(factors)):
        total1 += (factors[i]*(ceil((start-1)/factors[i]))*(ceil((start-1)/factors[i]+1))/2)
        if i>0:
            common = common*factors[i]//gcd(factors[i], common)
        else:
            common = factors[i]

    if len(factors) > 1:
        total1 -= (common*ceil(((start-1)/common))*ceil(((start-1)/common+1))/2)
    print(total1)

    total -= total1

    if total:
        return int(total)
        print(total)
    return -1

