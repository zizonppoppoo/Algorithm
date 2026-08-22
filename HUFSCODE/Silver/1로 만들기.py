import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
dp = [-1 for _ in range(N+1)]
dp[N] = 0

queue = deque([])
queue.append(N)

while queue:
    num = queue.popleft()
    if num == 1: break

    if num % 3 == 0 and dp[num//3] == -1:
        queue.append(num//3)
        dp[num//3] = dp[num] + 1
    if num % 2 == 0 and dp[num//2] == -1:
        queue.append(num//2)
        dp[num//2] = dp[num] + 1
    if dp[num-1] == -1:
        queue.append(num-1)
        dp[num-1] = dp[num] + 1

print(dp[1])