import sys
input = sys.stdin.readline

arr = []
N = int(input())
result = [0] * N
x = list(map(int, input().split()))
count = 0

for i in range(N):
    arr.append((x[i],i))

arr.sort()
for i in range(1,N):
    if arr[i][0] == arr[i-1][0]:
        result[arr[i][1]] = count
    else:
        count += 1
        result[arr[i][1]] = count
for x in result:
    print(x,end = " ")