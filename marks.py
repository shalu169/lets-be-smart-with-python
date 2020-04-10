nm = input().split()
n = int(nm[0])
m = int(nm[1])
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
k = int(input())
print(arr)
m = sorted(arr, key=lambda x: x[k])
for a in m:
    print(*a)

