n = int(input())
DP = [1,3]
for i in range(3,n+1):
    DP.append((DP[i-3]*2 + DP[i-2]) % 10007)
print(DP[n-1])