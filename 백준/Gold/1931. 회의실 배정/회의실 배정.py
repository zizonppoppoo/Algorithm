N = int(input())
arr = []
for i in range(N):
    n, m = map(int, input().split())
    arr.append((n,m))

arr.sort(key=lambda x: (x[1], x[0]))
count = 1
end = arr[0][1]

for i in range(1,N):
    if arr[i][0] >= end:
        count += 1
        end = arr[i][1]

print(count)