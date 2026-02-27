import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
timeline = [[0, 0] for _ in range(n)]

for i in range(n):
    T, P = map(int, input().split())
    timeline[i][0] = T
    timeline[i][1] = P

for i in range(n-1,-1,-1):
    if timeline[i][0] > n-i:
        dp[i] = dp[i+1]
    elif timeline[i][0] <= n-i:
        dp[i] = max(timeline[i][1]+dp[i+timeline[i][0]], dp[i+1])
print(dp[0])