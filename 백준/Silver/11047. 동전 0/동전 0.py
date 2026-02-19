import sys

n, k = map(int, sys.stdin.readline().split())
coin_list = [0] * n
count = 0

for i in range(n):
    coin = int(input())
    coin_list[i] = coin

for i in range(n-1, -1, -1):
    if coin_list[i] <= k:
        count += k//coin_list[i]
        k -= (k//coin_list[i]) * coin_list[i]

    if k == 0:
        break
print(count)