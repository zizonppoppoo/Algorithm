import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

left = max(arr)
right = sum(arr)
result = right

while left <= right:
    mid = (left + right) // 2

    count = 1
    total = 0

    for i in arr:
        if total + i > mid:
            count += 1
            total = i
        else:
            total += i

    if count <= m:
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)