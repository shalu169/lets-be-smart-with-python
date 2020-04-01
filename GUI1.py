import math


def squares(a, b):
    count = 0
    for i in range(a,b+1):
        p = i**.5
        print(p)
        inti = int(p)
        deci = p- inti

        if deci == 0:
            count = count + 1
    print(count)
squares(1,10)