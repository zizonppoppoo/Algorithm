import sys
input = sys.stdin.readline

n = int(input())
points = [0] + [int(input()) for _ in range(n)]

if n == 1:
    print(points[1])

elif n == 2:
    print(points[1] + points[2])

else:
    dp = [0] * (n + 1)
    dp[1] = points[1]
    dp[2] = points[1] + points[2]
    dp[3] = max(points[1] + points[3], points[2] + points[3])

    for i in range(4, n + 1):
        dp[i] = max(dp[i-2] + points[i], dp[i-3] + points[i-1] + points[i])
    print(dp[n])