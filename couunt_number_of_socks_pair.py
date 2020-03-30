def sockMerchant(n, ar):
    count = 0
    ar1 = set(ar)
    print(ar1)
    for i in ar1:
        p = ar.count(i)
        print(p)
        count = count + int(p/2)
    return count


n = int(input("enter number of input"))
ar = list(map(int,input().split()))
print(sockMerchant(n, ar))
