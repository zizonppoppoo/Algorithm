import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
left = 0
right = 0
result = 0

for i in arr:
    if i > right:
        right = i

while left <= right:
    count = 0
    mid = (left+right)//2
    for i in arr:
        if i - mid > 0:
            count += i - mid
    if count < M:
        right = mid - 1
    elif count >= M:
        if result < mid:
            result = mid
        left = mid + 1
print(result)