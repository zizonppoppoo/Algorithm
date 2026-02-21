import math
n, m = map(int, input().split())
arr = []

for i in range(m+1):
    arr.append(i)

arr[1] = 0

for i in range(2,int(math.sqrt(m)+2)):
    if arr[i] == 0:
        continue
    for j in range(i+i, m+1,i):
        arr[j] = 0

for i in range(n, m+1):
    if arr[i] != 0:
        print(arr[i])