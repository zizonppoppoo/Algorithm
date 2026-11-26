import sys
input = sys.stdin.readline

N = int(input())
table = []
DP = [0] * N

for _ in range(N):
    t, p = map(int, input().split())
    table.append((t, p))

if table[N-1][0] == 1:
    DP[N-1] = table[N-1][1]

for i in range(N-2, -1, -1):
    if table[i][0] == 1:
        DP[i] = table[i][1] + DP[i+1]
    else:
        if table[i][0] < N-i:
            DP[i] = max(DP[i+1], table[i][1] + DP[i+table[i][0]])
        elif table[i][0] == N-i:
            DP[i] = max(DP[i+1], table[i][1])
        else: DP[i] = DP[i+1]

print(max(DP))

# DP[n] = N일