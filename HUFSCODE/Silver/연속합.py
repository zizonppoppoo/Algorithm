import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]]

for i in range(1,n):
    if dp[i-1] + arr[i] > 0: dp.append(dp[i-1] + arr[i])
    else: dp.append(arr[i])

result = dp[0]
for num in dp:
    if num > result: result = num

print(result)